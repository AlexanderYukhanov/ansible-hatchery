
rm -rf $HOME/ansible-hatchery/prs
rm -rf $HOME/ansible-hatchery/role
rm -rf $HOME/ansible-hatchery/all
rm -rf $HOME/ansible-hatchery/template

cd $HOME/azure-rest-api-specs/specification/sql/resource-manager
autorest --output-folder=$HOME/ansible-hatchery --use=$HOME/autorest.ansible --python --tag=package-2017-03-preview

cd $HOME/azure-rest-api-specs/specification/mysql/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2017-04-preview

cd $HOME/azure-rest-api-specs/specification/postgresql/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2017-04-preview

cd $HOME/azure-rest-api-specs/specification/authorization/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2015-07

cd $HOME/azure-rest-api-specs/specification/web/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2016-09

cd $HOME/azure-rest-api-specs/specification/network/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2017-10

cd $HOME/azure-rest-api-specs/specification/containerinstance/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2017-10-preview

cd $HOME/azure-rest-api-specs/specification/containerregistry/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2017-10

cd $HOME/azure-rest-api-specs/specification/keyvault/resource-manager
autorest --output-folder=$HOME/ansible-hatchery/ --use=$HOME/autorest.ansible --python --tag=package-2016-10

cp $HOME/ansible-hatchery/python/prs/* $HOME/ansible-hatchery/prs/
cp $HOME/ansible-hatchery/python/role/* $HOME/ansible-hatchery/role/
cp $HOME/ansible-hatchery/python/all/* $HOME/ansible-hatchery/all/
cp $HOME/ansible-hatchery/python/template/* $HOME/ansible-hatchery/template/
rm -rf $HOME/ansible-hatchery/python
