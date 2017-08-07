## yifi on commandline

Command line tool for browsing and downloading the yts torrents 

#### Installation
    
    pip install yifi

##### usage options 

    -id <number>      get the details of movie
    -s  <r or s>      sort by rating 
    -l  <number>      list length (max of 50)
    -p  <number>      page number
    -f  <string>      find query term
    -m  <number>      minimum rating (max 10)

    --download        downloads the torrent file
    --magnet          downloads the movie using the magnet
 
##### usage examples
first simply get the list top seeded and latest movie torrent by
        
        $yifi

the output has 2 columns **movie_id** and **movie_title**

if you want the further page results go for 
    
        $yifi -p 2 
        $yifi -p 5

once you have the id you can view the details of the movie by simply
    
        $yifi -id movie_id
    
to search the movie in yifi database 
    
        $yifi -f <move_name>
   
and when you want to download the movie go with
    
        $yifi -id <movie_id> --download

this would download the **.torrent** file 

to download the movie using the torrent do
    
        $yifi -id <movie_id> --magnet
