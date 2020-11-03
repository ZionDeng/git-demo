a =1 
# add another comment
# use vs code to git 
# changed in dev branch 


# %% branch 

# git checkout -b branch_name -> build a branch and switch to it

# %% merge 
# git checkout dev -> create a dev branch and switch to it 
# git checkout master -> back to master branch 
# # $ git merge --no-ff -m "keep merge info" dev: merge 2 branches into master, with log info 

# %% conflict situation 

# we have 2 branch now, panda and dev
# git merge dev -> see the conflict 
# edit in master and dev

# %% rebase 
# master added rebase stuff 
# git rebase dev --> but it is dangerous 

# %% stash temporary revise

# doing things, boss' temp job
# $ git stash -> save temporarily 
# be used to debug, lovely boss 

# $ git stash pop to get the changes back 

# %% link github 
# add a repo in github, don't add the README file
# $ git remote add origin [link]
# $ git push -u origin master

# you can view history code and so on 
# commit changes, then 
# $ git push -u origin master -> view on github