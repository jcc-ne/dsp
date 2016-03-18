# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
`pushd <dirname>` : save current dir and go to <dirname>
`popd`: go to dir in stack
`dirs`: check dirs in stack
`cp`: copy file
`mkdir -p a/b/c`: make new directories recursively
`|`: pipe
`env`: show environment variables
`touch`: new file
`find . -name "*.txt"`: find .txt files
`exit`: exit terminal




---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
`ls`: list files in the current dir
`ls -a`: list files in the current dir, including hidden files
`ls -l`: list files in the current dir, list details
`ls -lh`: list files in the current dir, list details, human readable file types
`ls -lah`: list files in the current dir, list details, human readable file types, including hidden files
`ls -t`: list files in the current dir, sort by time
`ls -Glp`: list files in the current dir, list details, show '/' if it's a dir, color output


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
`ls -lt`: list includes modified time and details
`ls -lu`: list includes last access time and details
`ls -lU`: list includes created time and details
(add -r tag to reverse order)
`ls -F`: display more symbols '/' for dir, @ for symlink
`ls -R`: show files recursively



---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > execute passes args . I use it to catch Zombie process and kill

ps ux |awk -F' ' '{if ($8~/Z/) print $2}'|xargs -n1 -p kill

