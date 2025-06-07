git add .
read -p "Enter commit message:" commitmsg
git commit -m "$commitmsg"
git push
python3 main.py
