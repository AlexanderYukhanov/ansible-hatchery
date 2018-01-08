cd ~/ansible-hatchery
git checkout master
git pull

cd ~/azure_preview_modules
git checkout hatchery-pr-branch 2>/dev/null || git checkout -b hatchery-pr-branch;
git pull
cp -rfv ~/ansible-hatchery/role/modules/* ~/azure_preview_modules/library
cp -rfv ~/ansible-hatchery/role/tests/* ~/azure_preview_modules/tests/integration/targets

git add -A
git commit -m "updated modules"
git push --repo=https://$GIT_USER:$GIT_PASSWORD@github.com/Azure/azure_preview_modules.git hatchery-pr-branch
