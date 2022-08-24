
## Creacion del ambiente
python -m pip install venv
python -m venv grafana2uim
source grafana2uim/bin/activate

#######
…or create a new repository on the command line
echo "# grafana2uim" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:n3krodamus/grafana2uim.git
git push -u origin main

####
…or push an existing repository from the command line
git remote add origin git@github.com:n3krodamus/grafana2uim.git
git branch -M main
git push -u origin main

