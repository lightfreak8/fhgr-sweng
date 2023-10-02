
# push
```sh
git add "filename"
git status
git commit -m "blabla"
git push
```

# pull -> go to desired location
```sh
git pull
```

# git branching

- list local branches `git branch`
- list remote branches `git branch -r`
- list all branches `git branch -a`
- create branch `git branch BRANCH_NAME`
- switch to branch `git checkout BRANCH_NAME`
- create branch and switch `git checkout -b BRANCH_NAME`
- merge branches **into current branch (`git checkout ...`)** one `git merge BRANCH_NAME`
- rename branch `git branch -m OLD_NAME NEW_NAME`
- delete branch `git branch -d BRANCH_NAME`

## order of commands when creating a feature
1. `git checkout -b FEATURE_NAME`
2. add feature through code
3. `git checkout dev`
4. `git merge FEATURE_NAME`

# vscode
```
ctrl + j = display terminal
ctrl shift + k v = live mermaid tab
ctrl + k = mermaid view
```
