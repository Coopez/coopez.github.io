# Local preview at http://localhost:4000 — needs Docker Desktop running, no Ruby install.
#
# Why not `jekyll serve`? On Windows it leaves the page unstyled: `serve`
# force-rewrites the site url to the --host value (http://0.0.0.0:4000), and
# Windows browsers won't load assets from 0.0.0.0. So instead we BUILD with
# _config_docker.yml (url:"") — which makes asset links root-relative — then
# serve the static _site/ folder with a plain webrick file server that doesn't
# rewrite anything. `--watch` rebuilds on save; refresh the browser to see edits.
# ponytail: --force_polling because file-change events don't cross the Windows/Linux mount.

$cmd = "bundle install && " +
       "bundle exec jekyll build --config _config.yml,_config_docker.yml && " +
       "(bundle exec jekyll build --config _config.yml,_config_docker.yml --watch --force_polling >/dev/null 2>&1 &) && " +
       "bundle exec ruby -run -e httpd _site -p 4000 --bind-address=0.0.0.0"

docker run --rm -it -p 4000:4000 -v "${PWD}:/site" -w /site -e BUNDLE_PATH=/site/.bundle ruby:3.3 sh -c $cmd
