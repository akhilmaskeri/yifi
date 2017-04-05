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
        
        $python yifi

the output has 2 columns **movie_id** and **movie_title**

if you want the further page results go for 
    
        $python yifi -p 2 
        $python yifi -p 5

once you have the id you can view the details of the movie by simply
    
    $python yifi -id movie_id
    
and when you want to download the movie go with
    
    $python yifi -id <movie_id> --download

this would download the **.torrent** file 

to download the movie using the torrent do
    
    $python yifi -id <movie_id> --magnet
