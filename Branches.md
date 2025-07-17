# Git Branches


## List current branches
```bash
# List local branches
git branch
```

```bash
# List all branches including remote branches 
git branch -a
```


## Create a new branch

There are a few ways to do it in Git:

### 1. (old way)
```bash
# Create a new branch "dev" and switch to it
git checkout -b dev
``` 

### 2. 
```bash
# Create a new branch
git branch dev

# Switch to the new branch
git switch dev
```

### 3.
```bash
# Create a new branch "dev" and switch to it in one command:
git switch -c dev
```


## Switch between branches
```bash
git switch <branch_name>
```

or (traditional way)

```bash
git checkout <branch_name>
```
