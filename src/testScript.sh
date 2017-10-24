TARGET_DIR='/home/pi/'
for directory in ${TARGET_DIR}*;
do
  echo date
  if [ -f "$directory" ] ; then
    size=`ls -l $directory |cut -d" " -f5`
    echo " ${directory##*/} --- $size"
  fi
done
