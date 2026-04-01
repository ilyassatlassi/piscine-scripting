TZ=utc ls -l --time-style='+%F %R' | awk '{print $1, $6, $7, $8}' |sed 1d 
