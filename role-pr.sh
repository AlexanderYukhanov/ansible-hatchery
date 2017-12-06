cd ~/ansible-hatchery
git pull

cd ~/preview-modules
git checkout hatchery-pr-branch 2>/dev/null || git checkout -b hatchery-pr-branch;

cp -rfv ~/ansible-hatchery/role/modules/* ~/preview-modules/library
cp -rfv ~/ansible-hatchery/role/tests/* ~/preview-modules/tests/integration/targets

git add -A
git commit -m "updated modules"
git push --set-upstream origin hatchery-pr-branch
