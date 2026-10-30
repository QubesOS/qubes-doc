#!/bin/sh
# Some distributions (Fedora) patch sphinx_rtd_theme to load its fonts from
# /.sysassets/fonts/..., which only works on their documentation server.
# Copy those fonts from the system next to the CSS and use relative URLs, so
# the HTML also works when opened as local files.
# Usage: bundle-fonts.sh HTML_DIR
set -e
css_dir="$1/_static/css"
urls=$(grep -oh "/\.sysassets/fonts/[^')\"]*" "$css_dir"/*.css | sort -u)
[ -n "$urls" ] || exit 0
mkdir -p "$css_dir/fonts"
for url in $urls; do
    name=$(basename "$url")
    font=$(find /usr/share/fonts -name "$name" -print -quit)
    if [ -z "$font" ]; then
        echo "bundle-fonts: $name not found, leaving $url" >&2
        continue
    fi
    cp -L "$font" "$css_dir/fonts/$name"
    sed -i "s|$url|fonts/$name|g" "$css_dir"/*.css
done
