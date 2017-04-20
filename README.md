## yifi on commandline

###### options 
    -id <number>      get the details of movie
    -s  <r or s>      sort by rating 
    -o  <a or d>      order by ascending or descending 
    -l  <number>      list length (max of 50)
    -p  <number>      page number
    -f  <string>      find query term
    -g  <geners>      search by geners
    -m  <number>      minimum rating (max 10)

    --url             displays the URL hit 
    --download        downloads the torrent file
    --magnet          downloads the movie using the magnet
 

first simply get the list top seeded and latest movie torrent by
        
        $yifi

the output has 2 columns **movie_id** and **movie_title**

to search the movie in yifi database 
    
        $yifi -f <move_name>

if you want the further page results go for 
    
        $yifi -p 2 
        $yifi -p 5

once you have the id you can view the details of the movie by simply
    
        $yifi -id movie_id
    
and when you want to download the movie go with
    
        $yifi -id <movie_id> --download

this would download the **.torrent** file 

to download the movie using the torrent do
    
        $yifi -id <movie_id> --magnet
