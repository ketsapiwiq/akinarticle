input="../../bafe/bafe_articles.uris"

while IFS= read -r line
do
    echo "Trying with $line"
    outDir=$(basename "$line" | tr / _)
    echo "saving in dir $outDir"
    wget -nc -p $line -P ../articles/html/bafe/$outDir
    warcit $line ../articles/html/bafe/$outDir
    echo "saved and warc-ed $outDir"
done < "$input"