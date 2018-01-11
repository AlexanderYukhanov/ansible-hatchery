cd ~/ansible-hatchery
git pull
cd ~/ansible-hatchery/python/lib/ansible/modules/cloud/azure

for f in $1*
do
  echo "Processing $f"
  name=$(echo $f | cut -f 1 -d '.')
  cp -v ~/ansible-hatchery/role/modules/$name.py ~/ansible/lib/ansible/modules/cloud/azure/$name.py
  cp -v -r ~/ansible-hatchery/role/tests/$name ~/ansible/test/integration/targets 

  ansible-test integration -v --allow-destructive $name

done

cd ~
