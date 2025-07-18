from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Word Count Example") \
    .getOrCreate()
text_rdd = spark.sparkContext.textFile("C:/Users/DELL/Desktop/C-DAC Internship Tasks/sample.txt")
words_rdd = text_rdd.flatMap(lambda line: line.split())
word_pairs = words_rdd.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)
for word, count in word_counts.collect():
    print(f"{word}: {count}")
spark.stop()
