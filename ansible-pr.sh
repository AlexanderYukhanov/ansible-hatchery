if [ ! -d "~/$1" ]; then
    echo "CLONING ansible repo"
    git clone --recursive https://github.com/VSChina/ansible.git ~/$1
    cd ~/$1
    git checkout $1 2>/dev/null || git checkout -b $1;
fi

cd ~/$1
git pull
cp ~/ansible-hatchery/prs/modules/$1.py ~/$1/lib/ansible/modules/cloud/azure/$1.py
cp -v -r ~/ansible-hatchery/prs/tests/$1 ~/$1/test/integration/targets
git add -A
git commit -m "updates to $1"
git push --set-upstream origin $1
