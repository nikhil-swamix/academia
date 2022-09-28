#-----------------------------
#in Console Type this below
#-----------------------------

app.__vue__.$store._vm._computedWatchers.event_listener.deep=true;
app.__vue__.$store._vm._computedWatchers.event_listener.sync=true;
app.__vue__.$store._vm._computedWatchers.event_listener.active=false;


app.__vue__.$store._vm._computedWatchers.tab_change.deep=true;
app.__vue__.$store._vm._computedWatchers.tab_change.sync=true;
app.__vue__.$store._vm._computedWatchers.tab_change.lazy=false;
app.__vue__.$store._vm._computedWatchers.tab_change.active=false;
app.__vue__.$store._vm._computedWatchers.tab_change.value=[]


#-----------------------------
app.__vue__.$store._actions.emptyTabChangeArray[0]()
app.__vue__.$store._actions.appendTabChange[0]('apple')

# ROOT MODULE
app.__vue__.$store._modules.root._rawModule.modules.quizz.state.tab_change_array=['apple']