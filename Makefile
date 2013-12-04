USER=bdmorris
STEPS=ab en kw tm
all: $(foreach step, $(STEPS), results/$(step)-small.txt results/$(step)-large.txt)

results:
	mkdir -p results

results/%-small.txt: results %/mapper.py %/reducer.py
	cd $* && \
	../run_on_hadoop /odum/Odum_Local_Archive_all_ddi.xml /user/$(USER)/$*-small
	hadoop fs -cat /user/$(USER)/$*-small/part-00000 > $@
	hadoop fs -rmr /user/$(USER)/$*-small

results/%-large.txt: results %/mapper.py %/reducer.py
	cd $* && \
	../run_on_hadoop /odum/Odum_Archive_all_ddi.xml /user/$(USER)/$*-large
	hadoop fs -cat /user/$(USER)/$*-large/part-00000 > $@
	hadoop fs -rmr /user/$(USER)/$*-large
