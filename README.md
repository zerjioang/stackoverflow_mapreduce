# MapReduce - Apache Hadoop

## Dataset download

Example dataset is downloaded from https://archive.org/details/stackexchange.
As an example biology dataset download is shown:
```
wget https://archive.org/download/stackexchange/biology.stackexchange.com.7z
```

## Automatic dataset download & unpack
```
python2 ./downloader.py
```

## Running MapReduce algorithm without Hadoop:
```
chmod +x ./runme.sh
./runme.sh
```

## Running MapReduce algorithm with Hadoop:

As simple as:

```
hadoop fs -put ./out/Posts.xml
hs ./mapper.py ./reducer.py ./out/Posts.xml result
hadoop fs -ls result
hadoop fs -get result/part-00000
cat part-00000
```