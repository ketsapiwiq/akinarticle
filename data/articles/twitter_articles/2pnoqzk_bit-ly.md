---
title: "Brain Magazine"
url: http://bit.ly/2pnoqZK
keywords: url,magazine,efunctionreturn,uthisanalyticssiffunctiontypeof,send,eperformancefunctiontypeof,onew,brain,truereturn,uobjectucheckeruobjectucheckerifuasyncuobjectugetterfunctioneihitterhitvalueetypeuidelseifucbiucbtrthishitterhitvalueuobjectugettertypeuidifn_siteperformanceentriesenabledobjecttypeof,xiti,uthisaasyncdetectionfunctionuhitterhittypeadbackgoogleanalyticsvalueitracking_idanonymize_iptruefull_referrerdocumentreferrerextra_url_parametersnew_visitrgetsessionpageviewcount1randommathfloormathrandom1e41elsethistriggergoogleanalyticshittithishitteronloadfunctionstriggerstatsanalyticstiiffalsevar
---
\')}},multiSync:function(e){if(this.shouldSync(\"id5\")){var n=this;i.getConsentData(function(i){var o={external:true,type:\"user-sync\",provider:\"id5\",guestId:t.user.id,gdpr:null!==i?1:0,consentData:i,protocol:r.getProtocol(),end\_point:\"knitwears\",sub\_domain:\"www.brain-magazine.fr\"};e.getDistantData(o,n.printResponse.bind(n))})}},shouldSync:function(t){var r=t+\"Sync\";var i=Math.floor(Date.now()/1e3);var o=n.getItem(r,function(e){return parseInt(e)},function(){var e=i-24\*60\*60+1.5\*60;n.setItem(r,e);return e});if(i-o\<24\*60\*60&&-1===e.location.href.indexOf(\"adback\"+(t\[0\].toUpperCase()+t.substring(1))+\"ForceUpdate\")){return false}n.setItem(r,i);return true},printResponse:function e(t){if(t.length\>0){o(this.getElement(),\' \")}},getElement:function(){var t=e.document.querySelector(\".abusync\");if(null===t){t=e.document.createElement(\"div\");t.style.display=\"none\";t.className=\"abusync\";e.document.body.appendChild(t)}return t}}}},function(e,t){e.exports=function(e,t,n,r,i,o,a){return{data:null,status:0,init:function(){return this.detect().then(this.triggerEvent.bind(this)).then(this.initUser.bind(this));},detect:function(){return i.detect()},initUser:function(){if(!t.\_guid){return o.blocked()}return o.init().then(this.updateUser.bind(this))},updateUser:function(e){var i=e.user;var o=new r({tag\_version:t.\_tagVersion});if(i.id!==e.local.id&&(e.local.id!==null&&e.local.id!==undefined&&e.local.id!==false)){o.hit({value:e.local.id,type:\"Unify\"})}if(i.id!==e.api.id&&(e.api.id!==null&&e.api.id!==undefined&&e.api.id!==false)){o.hit({value:e.api.id,type:\"Unify\"})}n.push(a.track);return i.id},triggerEvent:function(e){this.status=e;for(var t in n){if(n.hasOwnProperty(t)){this.triggerCallback(n\[t\])}}n.push=this.triggerCallback.bind(this);n.unshift=this.triggerCallback.bind(this);return},triggerCallback:function(e){e(o.user.id,this.status,r)}}}},function(e,t){e.exports=function(e,t,n,r,i,o,a,s,u,l,c,f,d,h,p,g){return{Hitter:null,recheck:null,xitiPixelUrl:null,analytics:\[{id:\"Xiti\",object:s,checker:\"exists\",getter:\"notBlocked\"},{id:\"Gemius\",object:u,checker:\"exists\",getter:\"notBlocked\"},{id:\"Ghostery\",object:l,checker:\"present\",getter:\"present\"},{id:\"Ghostery\_Whitelist\",object:l,checker:\"present\",getter:\"isUrlWhiteListed\",async:true}\],init:function(){if(n.\_sitePerformanceEntriesEnabled&&\"object\"==typeof e.performance&&\"function\"==typeof e.performance.setResourceTimingBufferSize){e.performance.setResourceTimingBufferSize(500)}c.init();e.addEventListener(\"listsCompletedApi\",this.listsCompletedApi.bind(this));e.addEventListener(\"assetsCompletedApi\",this.assetsCompletedApi.bind(this));e.addEventListener(\"adbackRelaunchCheck\",this.relaunchCheck.bind(this));e.addEventListener(\"listsRecheck\",this.compileListRecheck.bind(this));this.run(false)},run:function(i){i=i\|\|false;if(i){if(undefined!==this.Hitter.reset){this.Hitter.reset()}}if(r.shouldSendTagData(n.\_tagChance)){t.unshift(this.triggerEvents.bind(this))}if(false){g.log(\"Launch xiti data sending\");null;t.push(this.sendToXiti.bind(this))}if(false){var o=Storage.getItem(\"oldAdblocker\",function(e){return\"true\"===e},function(){return false});if(true===o){e.sas\_target=e.sas\_target\|\|\"\";e.sas\_target+=\";adback\"}}},triggerEvents:function(t,i,o){var s=this;if(this.Hitter===null){this.Hitter=new o({tag\_version:n.\_tagVersion})}this.triggerStatsUser(t,i);if(false){var u=this;a.asyncDetection(function(){u.Hitter.hit({type:\"AdBackGoogleAnalytics\",value:i,tracking\_id:\"\",anonymize\_ip:true,full\_referrer:document.referrer,extra\_url\_parameters:{},new\_visit:r.getSessionPageViewCount()==1,random:Math.floor(Math.random()\*1e4+1)})})}else{this.triggerGoogleAnalyticsHit(t,i)}this.Hitter.on(\"load\",function(){s.triggerStatsAnalytics(t,i)});if(false){var l=0;var c=r.createAccurateInterval(function(){if(a.exist()){c.clear();s.Hitter.hit({value:+a.notBlocked(),type:\"GAnalytics\"})}else if(l\>15){c.clear();s.Hitter.hit({value:false,type:\"GAnalytics\"})}l++},100)}if(true){f.run(t,i)}if(true){h.syncUser(\"appnexus\",this.Hitter)}if(false){h.syncUser(\"rubicon\",this.Hitter)}if(false&&i\>0){p(e.document.body,\' \')}},triggerStatsUser:function e(t,n){if(false){this.Hitter.hit({value:n,type:\"AdBlock\"},i.displayFromResponse)}else{this.Hitter.hit({value:n,type:\"AdBlock\"})}if(n\>0){i.displayFromJson(\[\])}},triggerGoogleAnalyticsHit:function e(t,n){if(false&&(false\|\|false&&n\>0)){this.Hitter.hit({type:\"AdBackGoogleAnalytics\",value:n,tracking\_id:\"\",anonymize\_ip:true,full\_referrer:document.referrer,extra\_url\_parameters:{},new\_visit:r.getSessionPageViewCount()==1,random:Math.floor(Math.random()\*1e4+1)})}},listsCompletedApi:function e(t){this.Hitter.hit({value:+t.detail.bitmask,type:\"List\"})},assetsCompletedApi:function e(t){this.Hitter.hit({value:+t.detail.bitmask,type:\"Assets\"})},Ga:function(e,t){},sendToXiti:function(t,n,r){if(n\>0){g.log(\"Xiti send true\");null}else{g.log(\"Xiti send false\");null}var i=new CustomEvent(\"onAdbackReady\",{detail:{adblock:n\>0}});var o=new CustomEvent(\"AdbackReady\",{detail:{adblock:n\>0}});e.dispatchEvent(i);e.dispatchEvent(o)},triggerStatsAnalytics:function(t,r){var i=this;if(false===false){this.analytics.unshift({id:\"GAnalytics\",object:a,cb:\"Ga\",checker:\"exist\",getter:\"notBlocked\"})}for(var s in this.analytics){if(!this.analytics.hasOwnProperty(s)){continue}var u=this.analytics\[s\];if(\"function\"===typeof u.object\[u.checker\]&&u.object\[u.checker\]()){if(u.async){u.object\[u.getter\](function(e){i.Hitter.hit({value:+e,type:u.id})})}else{if(u.cb){i\[u.cb\](t,r)}this.Hitter.hit({value:+u.object\[u.getter\](),type:u.id})}}}if(n.\_sitePerformanceEntriesEnabled&&\"object\"==typeof e.performance&&\"function\"==typeof e.performance.getEntries){this.Hitter.hit({value:e.performance.getEntries().length,type:\"Performance\_Entries\"})}if(n.\_assetsCheck.length\>0){o.run(n.\_assetsCheck,\"assetsCompletedApi\")}if(n.\_listsUseEnabled&&this.shouldCheckLists(r)\|\|\"undefined\"!==typeof adbackDebug){o.run(n.\_lists,\"listsCompletedApi\")}if(this.shouldCheckConsent(r)\|\|\"undefined\"!==typeof adbackDebug){d.run(this.Hitter)}},relaunchCheck:function(){o.run(n.\_lists,\"listsRecheck\");c.detect().then(this.compileRecheck.bind(this))},shouldCheckLists:function(e){if(0===e){return false}var t=Storage.getItem(\"listTrack\",function(e){return e},function(){return false});if(false===t){Storage.setItem(\"listTrack\",1)}else if(1===t){Storage.setItem(\"listTrack\",2)}else if(2===t\|\|this.isRandomCheck()){Storage.setItem(\"listTrack\",3);return true}return false},shouldCheckConsent:function(e){var t=Storage.getItem(\"consentTrack\",function(e){return e},function(){return false});if(false===t){Storage.setItem(\"consentTrack\",1)}else if(1===t){Storage.setItem(\"consentTrack\",2)}else if(2===t\|\|this.isRandomCheck()){Storage.setItem(\"consentTrack\",3);return true}return false},isRandomCheck:function(){return Math.random()\<=.01},compileListRecheck:function(e){this.compileRecheck(e.detail.bitmask)},compileRecheck:function(t){if(null===this.recheck){this.recheck=t}else{var n=this.recheck+t;this.Hitter.hit({value:n,type:\"List\_Recheck\"});this.recheck=null;var r=new CustomEvent(\"ListRecheckCompleted\",{detail:{bitmask:n}});e.dispatchEvent(r)}},GAExistAndIsBlocked:function(){return\"function\"===typeof a\[\"exist\"\]&&a\[\"exist\"\]()&&\"function\"===typeof a\[\"notBlocked\"\]&&!a\[\"notBlocked\"\]()},sendATInternetPixel:function(e){this.xitiPixelUrl=e.replace(\"&ref=\",\"&sourceid=adback&ref=\");t.push(this.triggerATInternetPixel.bind(this))},triggerATInternetPixel:function(e,t,i){if(this.Hitter===null){this.Hitter=new i({tag\_version:n.\_tagVersion})}if(null===this.xitiPixelUrl){return}var o=this.xitiPixelUrl;if(-1===this.xitiPixelUrl.indexOf(\"idclient\")){o=this.xitiPixelUrl.replace(\"&ref=\",\"&idclient\"+e+\"&ref=\")}g.log(\"Proxy xiti on url \"+o);this.Hitter.hit({external:true,hit:false,type:\"proxified\_pixel\",url:o,protocol:r.getProtocol()});this.Hitter.hit({value:t,type:\"XitiProxification\"})}}}}\]);