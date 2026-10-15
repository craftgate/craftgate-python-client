#!/usr/bin/env bash
# Builds the package the way the release workflow does for version $1, without committing, tagging or publishing,
# installs the wheel into a fresh virtualenv and checks the x-client-version header. The check runs next to an
# unrelated _version.py, like an application that has its own, to make sure the client reads its own version.
set -euo pipefail
version="${1:?usage: release-dry-run.sh <version>}"
repo_dir="$(cd "$(dirname "$0")/../.." && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT

mkdir "$work_dir/source"
git -C "$repo_dir" archive HEAD | tar -x -C "$work_dir/source"
expected="$(python "$work_dir/source/scripts/update_version.py" "$version")"
python -m build --wheel --outdir "$work_dir/dist" "$work_dir/source"

python -m venv "$work_dir/venv"
"$work_dir/venv/bin/pip" install --quiet "$work_dir"/dist/*.whl

mkdir "$work_dir/app"
echo 'VERSION = "application-version"' > "$work_dir/app/_version.py"
cat > "$work_dir/app/check.py" <<'PY'
import sys

from craftgate import RequestOptions
from craftgate.adapter.base_adapter import BaseAdapter

adapter = BaseAdapter(RequestOptions(api_key="api-key", secret_key="secret-key", base_url="http://localhost"))
actual = adapter._create_headers(None, "/payment/v1/card-payments")["x-client-version"]
expected = "craftgate-python-client:" + sys.argv[1]
if actual != expected:
    sys.exit("Expected header %r, got %r" % (expected, actual))
print("OK x-client-version: " + actual)
PY
(cd "$work_dir/app" && "$work_dir/venv/bin/python" check.py "$expected")
