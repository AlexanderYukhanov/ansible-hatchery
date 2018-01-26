cd /ansible-hatchery
git pull
cd /autorest.ansible
git pull
npm run build
cd /ansible-hatchery
./generate.sh
