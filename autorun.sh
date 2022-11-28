set -e

cd /root/github/PushPoemToWife

git checkout dev
echo "now push $(date)" > log.log
git add .
git commit -am "push time: $(date)"
git push origin dev
