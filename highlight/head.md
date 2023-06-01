Merged to master and branch-3.4.
Merging to master/3.4
merged into master/3.4
merged into master/3.4.  Thank you @ulysses-you
cc @HyukjinKwon @ueshin
close this one in favor of https://github.com/apache/spark/pull/40006
late <font color=red><strong>LGTM</strong></font>
cc @JoshRosen  @liuzqt
We're closing this PR because it hasn't been updated in a while. This isn't a judgement on the merit of the PR in any way. It's just a way of keeping the PR queue manageable.<br>If you'd like to revive this PR, please reopen it and ask a committer to remove the Stale tag!
@HeartSaVioR , @HyukjinKwon , @SandishKumarHN PTAL. I would like to get this fix asap to make it into 3.4.x in OSS and 12.2 RC cut in DBR.
cc: @gengliangwang
<font color=red><strong>Thanks</strong></font>, merging to master/3.4
`DataFrame.drop` in PySpark seems problematic when there are duplicated column names, let me address it first.
@zhengruifeng what is the current problem with drop?
> @zhengruifeng what is the current problem with drop?<br><br>existing implement in Python Client follows the behavior in PySpark that always convert column name to column, then it has this problem https://issues.apache.org/jira/browse/SPARK-42444<br>
cc @hvanhovell @HyukjinKwon @xinrong-meng @amaliujia
cc @HyukjinKwon @xinrong-meng would you mind taking a look at this one?
cc @srowen, @dongjoon-hyun, @gengliangwang, @wangyum
cc @gengliangwang FYI
I did a quick <font color=red><strong>test</strong></font> and the UI looks ok. Also I tried git grep and all the old version `1.10.25` is gone.<br>@peter-toth <font color=red><strong>Thanks</strong></font> for the work. Merging to master.
> <font color=red><strong>LGTM</strong></font> if the UI works<br><br>I played a bit with the UI while making this PR and it looked ok to me.<br><br>Actually, I'm not sure that anything from our <font color=red><strong>customization</strong></font>s in `core/src/main/resources/org/apache/spark/ui/static/webui-dataTables.css` is still needed after this version update, but I removed only the up/dpwn arrows related part that caused issues...<br>E.g. the executor \"show ... entries\" box (https://github.com/apache/spark/pull/36226#issuecomment-1100810575) looked ok without this last fix: https://github.com/apache/spark/pull/36226/files#diff-e96c8dc10974b7da0c5dd4f675702462124b66c4bf2f7a0682f2ec1482a2eee3
> I did a quick <font color=red><strong>test</strong></font> and the UI looks ok. Also I tried git grep and all the old version `1.10.25` is gone. @peter-toth <font color=red><strong>Thanks</strong></font> for the work. Merging to master.<br><br><font color=red><strong>Thanks</strong></font> everyone for the <font color=red><strong>review</strong></font>!
cc @zhengruifeng IIRC there were some open questions to support storage level in Connect?
@HyukjinKwon can you please <font color=red><strong>check</strong></font> if it looks Ok?
@HyukjinKwon @amaliujia can you please <font color=red><strong>review</strong></font>? <br>If you think implementation of StorageLevel is not right I will close and can open a new one for the param only (when there's alternative implementation is <font color=red><strong>available</strong></font>). The problem is you cant just add something to PySpark without touching Connect. I guess it's intentional.
Closing as no traction
Sorry for late responses. We should better have this <font color=red><strong>feature</strong></font> parity. But I need to <font color=red><strong>check</strong></font> w/ the concern about storage level (raised internally). I will ping the guy to comment here.
<font color=red><strong>Thanks</strong></font> @HyukjinKwon
Hi @khalidmammadov, now that `Catalog` in Scala client including protobuf definition has been implemented at #40438, do you want to continue working on this?<br>Otherwise, I can take this over.<br><font color=red><strong>Thanks</strong></font>.
Hi, thanks for letting me know. I will look at it<br><br>On Mon, 3 Apr 2023, 21:15 Takuya UESHIN, ***@***.***> wrote:<br><br>> Hi @khalidmammadov <https://github.com/khalidmammadov>, now that Catalog<br>> in Scala client including protobuf definition has been implemented, do you<br>> want to continue working on this?<br>> Otherwise, I can take this over.<br>> <font color=red><strong>Thanks</strong></font>.<br>><br>> —<br>> Reply to this email directly, view it on GitHub<br>> <https://github.com/apache/spark/pull/40015#issuecomment-1494921787>, or<br>> unsubscribe<br>> <https://github.com/notifications/unsubscribe-auth/ACYJ3NHUQOOWBY4SFT7D3XDW7MVVDANCNFSM6AAAAAAU3TDHCU><br>> .<br>> You are receiving this because you were mentioned.Message ID:<br>> ***@***.***><br>><br>
The build was failing due to https://github.com/apache/spark/pull/40674 and now <font color=red><strong><font color=blue>fix</strong></font>ed</strong></font> by https://github.com/apache/spark/pull/40681<br><br>Rebased.
<font color=red><strong>Thanks</strong></font>! merging to master.
<font color=red><strong>Thanks</strong></font> @ueshin!
cc @cloud-fan
thanks, merging to master/3.4! (`multiTransform` is a to-be-released developer API)
<font color=red><strong>Thanks</strong></font> @cloud-fan for the <font color=red><strong>review</strong></font>!
Maybe @gengliangwang ?
cc @zhenlineo
For the <font color=red><strong>review</strong></font>ers. This is a mostly mechanical PR; the size is large but the complexity is low. All implemented <font color=red><strong>documentation</strong></font> and function signatures were copies from Dataset.
merging this!
Sorry about getting back and forth about the schema inference. I am trying to tell a good story about the timestamp without time zone. This should be the final version before 3.4.0 release.
@cloud-fan
Let's do this kind of <font color=red><strong>clean</strong></font>ing when we touch the codes around here next time.
Merged to master.
@zhenlineo can you make the PR description a bit more descriptive?
Oh and can you add the ticket to the title?
So it is ok to not have e2e <font color=red><strong>test</strong></font>s for read API (similarly for the write side)?
<font color=red><strong>LGTM</strong></font><br><br>Looks like you only need `./build/mvn -Pscala-2.12 scalafmt:format -Dscalafmt.skip=false -Dscalafmt.validateOnly=false -Dscalafmt.changedOnly=false -pl connector/connect/common -pl connector/connect/server -pl connector/connect/client/jvm` to fix the style.
merging.
FYI, bunch of Scala 2.13 <font color=red><strong>test</strong></font>s fail (https://github.com/apache/spark/actions/runs/4187249065/jobs/7256849374#step:9:19944) should be <font color=red><strong><font color=blue>fix</strong></font>ed</strong></font> before cutting RC cc @xinrong-meng
Hi, @hvanhovell .<br>Since we are close to RC1 cut, could you <font color=red><strong>test</strong></font> Scala 2.13 before merging your PR, please?<br>If there is the best person to do that, it's you, @hvanhovell . <font color=red><strong>:)</strong></font>
Thank you @HyukjinKwon @dongjoon-hyun
No, it was broken since Spark 3.3.0.
> cc @HyukjinKwon and @viirya Note that I don't think this is a blocker for 3.3.2 RC1 vote.<br><br>Hmm, I think you will back port it to branch-3.3? But we don't need to cut RC2 for it? Do you mean that?
Yes, I'll land this after your release, @viirya .
Thank you, @viirya . Let me open this until Tomorrow. <font color=red><strong>:)</strong></font>
Also, cc @xinrong-meng
Thank you, @viirya and @HyukjinKwon .<br><br>For the record, Apache Spark 3.3.2 RC1 vote passed. This patch will be delivered via Spark 3.4.0/3.3.3.<br>- https://lists.apache.org/thread/krnpf0tv1jdxy6dlssho1cn7ckfjwk2m
Attaching screenshots of the updated pages.<br><br><img width=\"1160\" alt=\"getting_started-install rst\" src=\"https://user-images.githubusercontent.com/112507318/218973521-6206edc3-abc5-481b-8c90-183fe0d82b7b.png\"><br><br><img width=\"1160\" alt=\"getting_started-quickstart_df ipynb\" src=\"https://user-images.githubusercontent.com/112507318/218973623-1d9e4e02-0b4a-42fa-aa87-b5dda72e64bc.png\"><br><br><img width=\"1160\" alt=\"reference-pyspark streaming rst\" src=\"https://user-images.githubusercontent.com/112507318/218973697-be6f786b-7c90-4bfb-a86f-1b870987a2b7.png\"><br><br><img width=\"1160\" alt=\"user_guide-index rst\" src=\"https://user-images.githubusercontent.com/112507318/218973758-e2d9b81a-63f9-43b0-8f72-1fb96f594ed7.png\"><br>
Late <font color=red><strong>LGTM</strong></font>, thank you @allanf-db !
@haoyanzhang It is better to create a separate branch per every PR:<br><img width=\"700\" alt=\"Screenshot 2023-02-16 at 12 54 49\" src=\"https://user-images.githubusercontent.com/1580697/219332108-0c909f7d-907c-46c3-b290-b70029675ea1.png\"><br><br>see \"Pull request\" at https://spark.apache.org/contributing.html
@haoyanzhang Do you have an account at OSS JIRA: https://issues.apache.org/jira ? If not, I'll create it for you.
> @haoyanzhang It is better to create a separate branch per every PR: <img alt=\"Screenshot 2023-02-16 at 12 54 49\" width=\"700\" src=\"https://user-images.githubusercontent.com/1580697/219332108-0c909f7d-907c-46c3-b290-b70029675ea1.png\"><br>> <br>> see \"Pull request\" at https://spark.apache.org/contributing.html<br><br>got it,  will do it next time
> @haoyanzhang Do you have an account at OSS JIRA: https://issues.apache.org/jira ? If not, I'll create it for you.<br><br>I have one, thanks
+1, <font color=red><strong>LGTM</strong></font>. Merging to master.<br>Thank you, @haoyanzhang and @HyukjinKwon for <font color=red><strong>review</strong></font>.
@haoyanzhang Congratulations with the first <font color=red><strong>contribution</strong></font> to Apache Spark!
cc @HyukjinKwon
Thank you, @yaooqinn , @HyukjinKwon , @LuciferYang .
So now we can <font color=red><strong>upgrade</strong></font> guava?
Not yet, @bjornjorgensen ~ <font color=red><strong>:)</strong></font> Please hold on any significant <font color=red><strong>c<font color=blue>hang</strong></font>es</strong></font> until Apache Spark 3.4 is released. We still need to backport many bug fixes during Apache Spark 3.4 RC period. Here I just removed the broken CI which no one will take care.
I remember Guava <font color=red><strong>upgrade</strong></font> is also blocked by Hive .. IIRC ..
cc @olaky
<font color=red><strong>Thanks</strong></font>, this is a helpful clarification
@cloud-fan @olaky Added more clarifications, let me know WDYT! <font color=red><strong>Thanks</strong></font>
<font color=red><strong>Thanks</strong></font>! updated
cc @cloud-fan Fixed the style, and passed all <font color=red><strong>check</strong></font>s, thanks!
thanks, merging to master/3.4!
cc @juliuszsompolski @cloud-fan FYI
kindly ping @HyukjinKwon @HyukjinKwon
thanks, merged to master and 3.4
<font color=red><strong>Thanks</strong></font> for fixing this. Merged to master and branch-3.4.
cc @zhenlineo we discussed this today
<font color=red><strong>Thanks</strong></font> for looking into this. We should definitely fix the leak. I would probably do the same:<br>When we close the session, we go through all buffers and close them. The Result and <font color=red><strong>clean</strong></font>er also holds some resources.
We can also just <font color=red><strong>clean</strong></font>-up the results. Part of the problem is that the E2E <font color=red><strong>test</strong></font> does not close results. I am not sure if there are similar issues on the server side.
Will submit a PR shortly.
@hvanhovell What about this? https://github.com/apache/spark/compare/master...zhenlineo:spark:allocator-memleak?expand=1 when a session is closed, we force to close all buffers.
Let me close this one, thanks @hvanhovell @zhenlineo
<font color=red><strong>Thanks</strong></font> @wangyum @dongjoon-hyun
@srielau could you take a look, pls?
Also, I'd like to share some <font color=red><strong>performance</strong></font> measurements from my local machine, using JMH:<br>code example:<br>```java<br>...<br>    @Benchmark<br>    public void convert_branch_master(Blackhole bh) {<br>        // Convert to unsigned<br>        for (int i = -10_000; i < 10_000; i++) {<br>            UTF8String convert = NumberConverter<br>                    .convert(UTF8String.fromString(String.<font color=red><strong>value</strong></font>Of(i)).getBytes(), 10, 16);<br>            bh.consume(convert);<br>        }<br><br>        // Convert to signed<br>        for (int i = -10_000; i < 10_000; i++) {<br>            UTF8String convert = NumberConverter<br>                    .convert(UTF8String.fromString(String.<font color=red><strong>value</strong></font>Of(i)).getBytes(), 10, -16);<br>            bh.consume(convert);<br>        }<br>    }<br>...<br><br>// the same code for SPARK-42399 branch<br>```<br><br>With Java 8, current PR even <font color=red><strong>speed</strong></font>s up the <font color=red><strong>performance</strong></font>:<br>```java<br># JMH version: 1.36<br># VM version: JDK 1.8.0_362, OpenJDK 64-Bit Server VM, 25.362-b00<br># VM invoker: /usr/local/Cellar/openjdk@8/1.8.0+362/libexec/openjdk.jdk/Contents/Home/jre/bin/java<br># Blackhole mode: full + dont-inline hint (auto-detected, use -Djmh.blackhole.autoDetect=false to disable)<br># Warmup: 5 iterations, 10 s each<br># Measurement: 5 iterations, 10 s each<br># Timeout: 10 min per iteration<br># Threads: 1 thread, will synchronize iterations<br># Benchmark mode: Average time, time/op<br><br><br><br>Benchmark                                           Mode  Cnt   Score   Error  Units<br>NumberConverterBenchmark.convert_branch_master      avgt   10  30.458 ± 1.638  ms/op<br>NumberConverterBenchmark.convert_branch_spark42399  avgt   10  22.857 ± 0.421  ms/op<br><br>```<br><br>With Java 11, implementation from master branch works more then 2 times <font color=red><strong>fast</strong></font>er than the same implementation with Java 8!<br>But there is not a big gap in <font color=red><strong>performance</strong></font> difference between master branch implementation and implementation from current branch. <br>```java<br># JMH version: 1.36<br># VM version: JDK 11.0.16.1, OpenJDK 64-Bit Server VM, 11.0.16.1+0<br># VM invoker: /usr/local/Cellar/openjdk@11/11.0.16.1/libexec/openjdk.jdk/Contents/Home/bin/java<br># Blackhole mode: full + dont-inline hint (auto-detected, use -Djmh.blackhole.autoDetect=false to disable)<br># Warmup: 5 iterations, 10 s each<br># Measurement: 5 iterations, 10 s each<br># Timeout: 10 min per iteration<br># Threads: 1 thread, will synchronize iterations<br># Benchmark mode: Average time, time/op<br><br>Benchmark                                           Mode  Cnt   Score   Error  Units<br>NumberConverterBenchmark.convert_branch_master      avgt   10  14.453 ± 1.082  ms/op<br>NumberConverterBenchmark.convert_branch_spark42399  avgt   10  17.956 ± 0.489  ms/op<br><br>```<br><br>With Java 17, implementation from master branch works more then 3 times <font color=red><strong>fast</strong></font>er than the same implementation with Java 8 and ~ 2 times <font color=red><strong>fast</strong></font>er then the same implementation with Java 11!<br>And here is a significant difference between master branch implementation and current branch (master branch is ~2x times <font color=red><strong>fast</strong></font>er...). <br>```java<br># JMH version: 1.36<br># VM version: JDK 17.0.4.1, OpenJDK 64-Bit Server VM, 17.0.4.1+1<br># VM invoker: /usr/local/Cellar/openjdk@17/17.0.4.1_1/libexec/openjdk.jdk/Contents/Home/bin/java<br># Blackhole mode: compiler (auto-detected, use -Djmh.blackhole.autoDetect=false to disable)<br># Warmup: 5 iterations, 10 s each<br># Measurement: 5 iterations, 10 s each<br># Timeout: 10 min per iteration<br># Threads: 1 thread, will synchronize iterations<br># Benchmark mode: Average time, time/op<br><br>Benchmark                                           Mode  Cnt   Score   Error  Units<br>NumberConverterBenchmark.convert_branch_master      avgt   10   8.410 ± 0.161  ms/op<br>NumberConverterBenchmark.convert_branch_spark42399  avgt   10  18.162 ± 0.036  ms/op<br>```
@hvanhovell
cc @sadikovi @HyukjinKwon
We discussed before and decided to keep prefersDate similar to a decimal config cc @HyukjinKwon
Hmm, I take a quick <font color=red><strong>check</strong></font>, do you mean the json option `prefersDecimal`?  It is inconsistent with other JSON data source options either https://github.com/apache/spark/blob/master/sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/json/JSONOptions.scala#L240 ... Users can make mistakes since they are used to data source options without `s` on the verb.<br><br>Shall we support `preferDecimal` and `prefersDecimal` in JSON, and use `prefer` in the new options of Spark 3.4?
im fine w/ that
I am curious why did we not do it from the beginning?
> I am curious why did we not do it from the beginning?<br><br>I didn't join the <font color=red><strong>discussion</strong></font>, but let's make the naming consistent before it is too late. There is only one exception `prefersDecimal` now.<br><br>
CC @HyukjinKwon @zhengruifeng
Attaching screenshots of the updated Migration Guides page and the new version <font color=red><strong>upgrade</strong></font> sub-page.<br><br><img width=\"1340\" alt=\"pyspark_migration_guides_doc_page\" src=\"https://user-images.githubusercontent.com/112507318/219209282-27bea6e8-beb5-4336-a6c1-7e91a011a225.png\"><br><br><img width=\"1340\" alt=\"pyspark_migration_guide_<font color=red><strong>upgrade</strong></font>_doc_page\" src=\"https://user-images.githubusercontent.com/112507318/219209350-bdbf18e4-e77b-414e-a19d-8e431fb2a60a.png\"><br>
Yeah, let's close. I don't think this is an issue.
Thank you, @HyukjinKwon and @rithwik-db .
cc @zhenlineo @LuciferYang
https://github.com/apache/spark/blob/7ee8a32077b09cb847b6ac41cdc5067cf7bd83e9/connector/connect/client/jvm/src/<font color=red><strong>test</strong></font>/scala/org/apache/spark/sql/connect/client/util/RemoteSparkSession.scala#L155-L159<br><br>should we remove this `try catch`? This may cover up some problems, but this may be another pr<br><br>
According to your comment, is it okay for me to merge, @LuciferYang ?
> According to your comment, is it okay for me to merge, @LuciferYang ?<br><br>ok to merge ~
<font color=red><strong>Thanks</strong></font>, @LuciferYang . Merged to master/3.4.<br>Thank you, @hvanhovell , @HyukjinKwon , @LuciferYang .
thanks for the <font color=red><strong>review</strong></font>, merging to master/3.4!
Interestingly, it passed locally while GitHub Action jobs keep failing.<br>```<br>$ build/sbt \"sql/<font color=red><strong>test</strong></font>Only *.OrcSourceV1Suite -- -z SPARK-11412\"<br>...<br>[info] All <font color=red><strong>test</strong></font>s passed.<br>[<font color=red><strong>success</strong></font>] Total time: 23 s, completed Feb 20, 2023, 12:54:28 PM<br>```
Since this happens in GitHub Action currently, I made a WIP PR for further <font color=red><strong>investigation</strong></font>. If it's valid, I'll convert it to the official PR separately from this PR.<br>- https://github.com/apache/spark/pull/40095
I closed my PR because the failure seems to happen more earlier than this commit.
Note for the <font color=red><strong>review</strong></font>er. I still want to add a couple of <font color=red><strong>test</strong></font>s for duplicate functions.
@dongjoon-hyun I will fix those today. I do think we should have a <font color=red><strong>discussion</strong></font> about this. Currently we have both maven and scala-2.13 that are not <font color=red><strong>test</strong></font>ed during CI. That seems wrong if both are apparently supported. The mental overhead of <font color=red><strong>test</strong></font>ing these manually is very high.
As for blocking other <font color=red><strong>community</strong></font> members severely, the same applies to the lack of <font color=red><strong>test</strong></font>ing of scala-2.13.
Fix for 2.13 has merged. I am going to hold this off until https://github.com/apache/spark/pull/40056 is merged.
merging
thanks all
Some info I searched about it: https://docs.docker.com/build/at<font color=red><strong>test</strong></font>ations/slsa-provenance/.
Thank you. The affected versions are the future releases (3.4.0/3.3.3/3.2.4) instead of the released version.
K8s Integration Tests passed. Merged to master/3.4/3.3/3.2.
cc @wangyum @srowen FYI
Could you <font color=red><strong>test</strong></font> against hadoop-2?
> Could you <font color=red><strong>test</strong></font> against hadoop-2?<br><br>Do same <font color=red><strong>check</strong></font> with -Phadoop-2<br><br>**Maven** <br><br>```<br>build/mvn <font color=red><strong>clean</strong></font><br>build/mvn <font color=red><strong>clean</strong></font> install -DskipTestes -pl resource-managers/yarn -am -Pyarn -Phadoop-2<br>build/mvn -D<font color=red><strong>test</strong></font>=none -DwildcardSuites=org.apache.spark.deploy.yarn.YarnClusterSuite -pl resource-managers/yarn <font color=red><strong>test</strong></font> -Pyarn -Phadoop-2<br>build/mvn <font color=red><strong>test</strong></font> -pl resource-managers/yarn -Pyarn -D<font color=red><strong>test</strong></font>.exclude.tags=org.apache.spark.tags.ExtendedLevelDBTest  -Phadoop-2<br>```<br><br>**SBT**<br><br>```<br>build/sbt <font color=red><strong>clean</strong></font> yarn/<font color=red><strong>test</strong></font> -Pyarn -D<font color=red><strong>test</strong></font>.exclude.tags=org.apache.spark.tags.ExtendedLevelDBTest -Phadoop-2<br>```<br><br><br>All <font color=red><strong>test</strong></font>s passed.<br><br>
Merged to master
Merged to master. <font color=red><strong>Thanks</strong></font> @LuciferYang
Thank you, @LuciferYang and @huaxingao !
<font color=red><strong>Thanks</strong></font> @huaxingao @dongjoon-hyun
@nija-at can you file a ticket in the JIRA (or ask me to do it), and add that to the title?
Can you also do this for the scala client?
Actually. Please open a JIRA and add JIRA id to the PR title along with module names (example: `[SPARK-xxxx][CONNECT][PYTHON]) accept user_agent in spark connect's connection string`)
@hvanhovell <br><br>> can you file a ticket in the JIRA (or ask me to do it), and add that to the title?<br><br>Done.<br><br>> Can you also do this for the scala client?<br><br>I'll do that as a separate change<br>
@dongjoon-hyun this time I have <font color=red><strong>test</strong></font>ed 2.13.
Merging.
Thank you so much, @hvanhovell and @cloud-fan !
For the <font color=red><strong>review</strong></font>s, I have manually <font color=red><strong>test</strong></font>ed this with 2.13.
Alright merging this.
> For the <font color=red><strong>review</strong></font>s, I have manually <font color=red><strong>test</strong></font>ed this with 2.13.<br><br>Thank you so much, @hvanhovell !
Merged to master/3.4 for Apache Spark 3.4.0. Thank you, @huaxingao and @viirya .<br><br>cc @MaxGekk since he filed SPARK-39859 originally.
<font color=red><strong>Thanks</strong></font> @dongjoon-hyun @viirya
cc @dongjoon-hyun @HyukjinKwon
Merged to master for Apache Spark 3.5. Thank you, @sadikovi and @HyukjinKwon .
cc @viirya
Thank you, @viirya !
The <font color=red><strong>test</strong></font>s passed in the GitHub Action. Merged to master<br>![Screenshot 2023-02-17 at 1 08 13 AM](https://user-images.githubusercontent.com/9700541/219601614-e84bf609-e8fd-4a0b-80b8-0afa5f41b457.png)<br><br>Merged to master/3.4.
It seems more complicated than I thought, I think we can simplify it in this way<br><br>In client:<br>```<br>    def sql(self, sqlQuery: str, args: Optional[Dict[str, str]] = None) -> \"DataFrame\":<br>        df = DataFrame.withPlan(SQL(sqlQuery, args), self)<br>        print(df.schema)   <- eagerly analyze the plan<br>        return df<br>```<br><br>In connect planner:<br>```<br>  private def transformSql(sql: proto.SQL): LogicalPlan = {<br>    // scalastyle:off println<br>    println(s\"invoke transformSql $sql\")<br>    session<br>      .sql(sql.getQuery, sql.getArgsMap.asScala.toMap)    <- directly invoke the spark session api<br>      .logicalPlan<br>  }<br>```<br><br><br>bin/pyspark --remote \"local[*]\"<br>```<br>>>> spark.sql(\"set spark.sql.adaptive.enabled=false\")<br>invoke transformSql query: \"set spark.sql.adaptive.enabled=false\"<br><br>StructType([StructField('key', StringType(), False), StructField('<font color=red><strong>value</strong></font>', StringType(), False)])<br>DataFrame[key: string, <font color=red><strong>value</strong></font>: string]<br>```
@cloud-fan @boneanxs could you please take a look if you find a time?
@Yikf can you provide a <font color=red><strong>test</strong></font> case, or at least the error stacktrace you hit in your environment?
@cloud-fan This case is the error that Apache kyuubi encountered when upgrading from spark 3.3.1 to 3.3.2, can see this [link](https://github.com/apache/kyuubi/actions/runs/4192366930/jobs/7268919556#step:6:2611) to find the error stacktrace.
updated, verified w/ kyuubi on spark 3.3.2 and all <font color=red><strong>test</strong></font>s passed<br>```<br>build/mvn <font color=red><strong>clean</strong></font> <font color=red><strong>test</strong></font> -pl :kyuubi-spark-connector-hive_2.12 -am -Pspark-3.3 -Dspark.version=3.3.2<br>```
kindly ping @cloud-fan , @boneanxs Any suggestions?
I have not followed the <font color=red><strong>c<font color=blue>hang</strong></font>es</strong></font> in this part of the code too much in a while - but this <font color=red><strong>specific</strong></font> PR will result in a different `jobId` each time the class is deserialized - I would expect that to cause issues with output formats ?
@mridulm <font color=red><strong>Thanks</strong></font> your <font color=red><strong>review</strong></font>, this is a nice question for me, `JobId` maybe is different when each time the class is deserialized.<br><br>How about this idea that `SparkHadoopWriterUtils.createJobTrackerID` to generate an ID for a job tracker, and the job tracker is <font color=red><strong>unique</strong></font>, JobId is constructed using a <font color=red><strong>unique</strong></font> tackerid when the class is deserialized.
@Yikf Agree - we only specify two parts for the `JobID` - the `String jtIdentifier` and `int id`.<br>We can persist those in the class - and make jobId a `transient lazy val` which recreates it each time.<br><br>Something like this instead:<br><br>```<br><br>  private[this] val jobIdParts: (String, Int) = {<br>    val id = SparkHadoopWriterUtils.createJobID(new Date, 0)<br>    (id.getJtIdentifier, id.getId)<br>  }<br><br>  @transient private lazy val jobId = new JobID(jobIdParts._1, jobIdParts._2)<br>```<br><br>Thoughts ?<br>
@mridulm Nice suggestion, and we can simplify to as follow since `int id` is <font color=red><strong>unique</strong></font>.<br><br>```scala<br>  private[this] val jobTrackerID = SparkHadoopWriterUtils.createJobTrackerID(new Date)<br>  @transient private lazy val jobId = new JobID(jobTrackerID, 0)<br>```
Hi, @cloud-fan . SPARK-41448 landed to master/3.3/3.2 and this is merge this to master/3.4 only. I'm wondering if we are planning backporting to branch-3.3 and 3.2.<br>- https://github.com/apache/spark/pull/38980#issuecomment-1346229161<br>
Also, cc @sunchao
@Yikf can you help to open a backport PR for 3.2/3.3? <font color=red><strong>Thanks</strong></font>!
> @Yikf can you help to open a backport PR for 3.2/3.3? <font color=red><strong>Thanks</strong></font>!<br><br>Sure
cc @dongjoon-hyun
I make another one build with maven 3.8.7 + cyclonedx-maven-plugin  2.7.4 https://github.com/LuciferYang/spark/actions/runs/4205904014/jobs/7298678641<br><br><img width=\"1074\" alt=\"image\" src=\"https://user-images.githubusercontent.com/1475305/219719321-dc1e6aa3-1a21-4e93-92ce-60cee921493b.png\"><br>
I mean in our GitHub Action repo. We are using CycloneDX 2.7.3, aren't we?<br><br>> I make another one build with maven 3.8.7 + cyclonedx-maven-plugin 2.7.4 https://github.com/LuciferYang/spark/actions/runs/4205904014/jobs/7298678641
Yes, we use CycloneDX 2.7.3. So I should not explain that 2.7.4 has such issue in the pr description, because it does not affect Spark now, am I right?
Please let me explain my intention more:<br><br>1. First of all, I want to update maven to 3.9.0(keep use CycloneDX 2.7.3), then I found the following error:<br><br>```<br>[ERROR] An error occurred attempting to read POM<br>org.codehaus.plexus.util.xml.pull.XmlPullParserException: UTF-8 BOM plus xml decl of ISO-8859-1 is incompatible (position: START_DOCUMENT seen <?xml version=\"1.0\" encoding=\"ISO-8859-1\"... @1:42) <br>    at org.codehaus.plexus.util.xml.pull.MXParser.parseXmlDeclWithVersion (MXParser.java:3423)<br>    at org.codehaus.plexus.util.xml.pull.MXParser.parseXmlDecl (MXParser.java:3345)<br>    at org.codehaus.plexus.util.xml.pull.MXParser.parsePI (MXParser.java:3197)<br>    at org.codehaus.plexus.util.xml.pull.MXParser.parseProlog (MXParser.java:1828)<br>    at org.codehaus.plexus.util.xml.pull.MXParser.nextImpl (MXParser.java:1757)<br>    at org.codehaus.plexus.util.xml.pull.MXParser.next (MXParser.java:1375)<br>    at org.apache.maven.model.io.xpp3.MavenXpp3Reader.read (MavenXpp3Reader.java:3940)<br>    at org.apache.maven.model.io.xpp3.MavenXpp3Reader.read (MavenXpp3Reader.java:612)<br>    at org.apache.maven.model.io.xpp3.MavenXpp3Reader.read (MavenXpp3Reader.java:627)<br>    at org.cyclonedx.maven.BaseCycloneDxMojo.readPom (BaseCycloneDxMojo.java:759)<br>    at org.cyclonedx.maven.BaseCycloneDxMojo.readPom (BaseCycloneDxMojo.java:746)<br>    at org.cyclonedx.maven.BaseCycloneDxMojo.retrieveParentProject (BaseCycloneDxMojo.java:694)<br>    at org.cyclonedx.maven.BaseCycloneDxMojo.getClosestMetadata (BaseCycloneDxMojo.java:524)<br>    at org.cyclonedx.maven.BaseCycloneDxMojo.convert (BaseCycloneDxMojo.java:481)<br>    at org.cyclonedx.maven.CycloneDxMojo.execute (CycloneDxMojo.java:70)<br>    at org.apache.maven.plugin.DefaultBuildPluginManager.executeMojo (DefaultBuildPluginManager.java:126)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.doExecute2 (MojoExecutor.java:342)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.doExecute (MojoExecutor.java:330)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:213)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:175)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.access$000 (MojoExecutor.java:76)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor$1.run (MojoExecutor.java:163)<br>    at org.apache.maven.plugin.DefaultMojosExecutionStrategy.execute (DefaultMojosExecutionStrategy.java:39)<br>    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:160)<br>    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:105)<br>    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:73)<br>    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:53)<br>    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:118)<br>    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:260)<br>    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:172)<br>    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:100)<br>    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:821)<br>    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:270)<br>    at org.apache.maven.cli.MavenCli.main (MavenCli.java:192)<br>    at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)<br>    at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)<br>    at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)<br>    at java.lang.reflect.Method.invoke (Method.java:498)<br>    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced (Launcher.java:282)<br>    at org.codehaus.plexus.classworlds.launcher.Launcher.launch (Launcher.java:225)<br>    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode (Launcher.java:406)<br>    at org.codehaus.plexus.classworlds.launcher.Launcher.main (Launcher.java:347)<br>```<br><br>I think We should see similar errors here: https://github.com/LuciferYang/spark/actions/runs/4206035140/jobs/7299042843 later<br><br>2. then I want to <font color=red><strong>test</strong></font> maven 3.9.0 + CycloneDX 2.7.4 couple of days ago, but there an error same as  `maven 3.8.7 + cyclonedx-maven-plugin 2.7.4`,  I think we should see it here: https://github.com/LuciferYang/spark/runs/11424487074 later<br><br>3. then I <font color=red><strong>test</strong></font> maven 3.9.0 + CycloneDX 2.7.5 today, there is no above issues(we can <font color=red><strong>check</strong></font> https://github.com/LuciferYang/spark/runs/11424568023 later).<br><br>So If I want to <font color=red><strong>upgrade</strong></font> Spark to use maven 3.9.0, I must <font color=red><strong>upgrade</strong></font> cyclonedx-maven-plugin to 2.7.5, I should <font color=red><strong>upgrade</strong></font> them in one or two pr? <br>
I'm trying to assess the issue. So, those combination issue is not the AS-IS Apache Spark issue in both master/branch-3.4, right?<br><br>FYI, Cyclone plugin 2.7.4 issue is a known one. When I started SBOM works, 2.7.4 was the las<font color=red><strong>test</strong></font> but was unusable across multiple ASF projects. That was the main reason I chose 2.7.3 instead of the la<font color=red><strong>test</strong></font> at that time. I'm not quite sure if 2.7.5 is <font color=red><strong>stable</strong></font> enough.<br><br>Anyway, we can apply this PR on `master` branch for Apache Spark 3.5.0 only separately from the Maven issue. Maven is also another big issues always.
Yeah, Spark 3.4.0 does not need this pr.<br><br>
If you don't mind, please allow me one or two days. I'll <font color=red><strong>check</strong></font> this during weekend~ Thank you for your patience always.
@dongjoon-hyun found a new issue related to 2.7.5: https://github.com/CycloneDX/cyclonedx-maven-plugin/issues/284<br><br><br>
Got it. Thank you for informing.
I think we should wait for 2.7.6 or higher to <font color=red><strong>test</strong></font> <font color=red><strong>usability</strong></font>, then we can reuse this jira. I will close this pr first, thanks @dongjoon-hyun
+1 for your decision, @LuciferYang . Thank you for letting me know before I started my work~ <font color=red><strong>:)</strong></font>
I'm hitting this when trying to build hadoop having updated maven via homebrew so as to get spark to work.  joy.
This PR is superseded by https://github.com/apache/spark/pull/40726 .
I think we should better file a JIRA.
Discussed this with @grundprinzip. Apparently the retries are kept so long intentionally. The fix here needs to occur differently. Closing this PR for now.
cc @HyukjinKwon mind taking a look when you find some time?
<font color=red><strong>Thanks</strong></font>, @HyukjinKwon !
Late <font color=red><strong>LGTM</strong></font>
wait https://github.com/apache/spark/pull/40065
Need to wait for a <font color=red><strong>stable</strong></font> CycloneDX version, close this first<br>
Addressed comments. @LuciferYang <br>And gentle ping @wangyum @sunchao: could you also take a look?
Add a conf `spark.sql.hive.dropPartitionByName.enabled` and two <font color=red><strong>test</strong></font>s. cc: @sunchao
Merged to master, thanks!
Thank youso much, @wecharyu, @sunchao and all!
I need to update golden files in this PR.
When you have some time, could you <font color=red><strong>review</strong></font> this, @viirya ? I want to merge this to proceed the further <font color=red><strong>investigation</strong></font>s.
Thank you so much always for your help, @viirya !<br>Merged to master for Apache Spark 3.5.
Some <font color=red><strong>test</strong></font>s always fail with <br>```<br>112 did not equal 104 Invalid stopIndex of a query context. Actual:SQLQueryContext(Some(1),Some(15),Some(15),Some(112),Some(select id from hive.`/home/runner/work/oss-spark/oss-spark/target/tmp/spark-9ff647b3-c1b5-449d-ae54-19a7f3baff9d`),None,None)<br>```<br>Length of string \"select id from hive.`/home/runner/work/oss-spark/oss-spark/target/tmp/spark-9ff647b3-c1b5-449d-ae54-19a7f3baff9d`\" is 113, so the last index is 112.<br><br>I guess that's because my folder name is `oss-spark`. The two `oss-` contains 8 chars, that's equal to 112 - 104.<br><br>https://github.com/WweiL/oss-spark/actions/runs/4235566927/jobs/7359363624<br><br>So I changed the [hard-coded length here](https://github.com/apache/spark/blob/b36d1484c1a090a33d9add056730128b9ba5729f/sql/hive/src/<font color=red><strong>test</strong></font>/scala/org/apache/spark/sql/hive/execution/SQLQuerySuite.scala#L1410) to a variable-length one.<br><br>@MaxGekk @srielau @itholic I found that this is related to the PR (https://github.com/apache/spark/pull/39977) you pushed / <font color=red><strong>review</strong></font>ed. Can you guys also take a look? <font color=red><strong>Thanks</strong></font>!
<font color=red><strong>Thanks</strong></font> for catching out, @WweiL !
@cloud-fan Can you merge this to master when you get a chance? Thank you!
thanks, merging to master!
Was this merged only to Spark 3.5 (master branch)? The JIRA ticket is not properly marked for fix version as well as status, and we need to make it clear to determine the version range to apply SPARK-42572.
> Was this merged only to Spark 3.5 (master branch)? The JIRA ticket is not properly marked for fix version as well as status, and we need to make it clear to determine the version range to apply [SPARK-42572](https://issues.apache.org/jira/browse/SPARK-42572).<br><br>Yes this was only merged to master. I've updated the version in SPARK-42572. BTW is there a way to quickly decide what's the version of the current master branch? I thought it was 3.4...
Sorry I seem to look at different JIRA ticket. SPARK-42484 contains the <font color=red><strong><font color=blue>fix</strong></font>ed</strong></font> version, 3.5.0. That said, SPARK-42572 only needs to be applied to master branch.
The kub <font color=red><strong>test</strong></font> is not related to this PR, I believe:<br>```<br>[info] org.apache.spark.deploy.k8s.integration<font color=red><strong>test</strong></font>.KubernetesSuite *** ABORTED *** (27 minutes, 35 seconds)<br>[info]   io.fabric8.kubernetes.client.KubernetesClientException: Failure executing: POST at: https://192.168.49.2:8443/api/v1/namespaces. Message: object is being deleted: namespaces \"spark-e7de0ffd81044f09afb2693a0e227a43\" already exists. Received status: <br>```
+1, <font color=red><strong>LGTM</strong></font>. Merging to master/3.4.<br>Thank you, @gengliangwang.
Move `SaveMode` to catalyst module is a break change, need add `ProblemFilters` to `MimaExcludes`
> Move `SaveMode` to catalyst module is a break change, need add `ProblemFilters` to `MimaExcludes`<br><br>I think we shouldn't make such breaking change?
> > Move `SaveMode` to catalyst module is a break change, need add `ProblemFilters` to `MimaExcludes`<br>> <br>> I think we shouldn't make such breaking change?<br><br>best to avoid
Depends on https://github.com/apache/spark/pull/40109 to get the correct error message for `create`.
Sorry late <font color=red><strong>LGTM</strong></font>
Before we try to use multiple task schedulers, why not fix the <font color=red><strong>parallel</strong></font>ism issues in the existing one. Moving from a locking everywhere approach, to an event loop should yield quite a throughput <font color=red><strong>improvement</strong></font>.
