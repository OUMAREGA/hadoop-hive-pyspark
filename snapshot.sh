#!/bin/sh

take()
{
     [ -z $1 ] && echo "Error: snapshot name not provided" && exit 1;
     [ -d snapshots/$1 ] && echo "Error: snapshot name already taken" && exit 1;

     docker-compose exec namenode bash -c "hdfs dfsadmin -allowSnapshot /user && hdfs dfs -createSnapshot /user $1 && hdfs dfs -copyToLocal /user/.snapshot/$2/* /snapshots/"
     
     [ $? -ne 0 ] && echo "Error: snapshot $1 couldn't be created" && exit 1;
      
     echo "Snapshot $1 successfully created"      
}

restore()
{
     [ -z $1 ] && echo "Error: snapshot name not provided" && exit 1;
     [ ! -d snapshots/$1 ] && echo "Error: snapshot not found" && exit 1; 
     
     echo -n "This action will override /user in your HDFS : confirm ? (y/N)"
     read answer
     
     [ "$answer" != "y" ] && exit 0;

     docker-compose exec namenode bash -c "hdfs dfs -put -f /snapshots/$1/* /user/"
     
     [ $? -ne 0 ] &&  echo "Error: snapshot $1 couldn't be restored" && exit 1;

     echo "Snapshot $1 successfully restored"
}

"$@"

if [ -z $1 ]
then

cat << EOT

-- HDFS snapshot utility --

Usage: ./snapshot.sh [action]

Supported actions are
take    <name>	take a snapshot (will be saved to /snapshots)
restore <name>  restore the named snapshot     

EOT
fi
