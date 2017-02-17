library(twitteR)
library(ROAuth)
library(plyr)
library(stringr)

#tutorial used "e1071" and "RTextTools" libraries.

setup_twitter_oauth("wJxO4kezM8jK8tV4zA8DH40s6","VlKrKgkctixFOtuez4km5wcVe7ZWi3eb9JqoHo6KH1RLx5hs0q","3242976804-NdbP9J8nyqyKWaYCwMgvMFasz3lKfR8mn4QoadL","UoRwSP17IfAY07BbmvHCeDKSVuEAzArU81dJPgJaH2VDl")

#######################################################
#Extracting from twitter
#######################################################

#*********Next steps:
#Collect a string of twitter handles into a vector of 250 each and run the for loop. So far each person has 80 tweets) 

#search term
#tweets = searchTwitter(": + #singapore", n=50, lang = "en")
#tweets = searchTwitter("#INFJ", n=10, lang = "en")

#######################################################
#Personality categories [Analysts]
#######################################################

intj = c("thetrudz","alphaintj","femaleintj_","elmyrx","joshk","intjofficial","outercircles","ttscoff","MoneySavingMom","CrispinBurke","andimJULIE","lum","pvineetha","ShamandalieSG",
         "omid","TheJennyLam","marketingwizdom","jwgoerlich","elysa","lillyrblx","INTX_Bob","intjRj","MajPro","dboudreau","yisforyogini","hethfen","sladey66","chasejace","raleene","SergeyBiryukov","CKristofic","benjaminspak","crgonzalez","AlphaChar","wonderwall7","inBloome","glenc","kellyykao","creativeintro",
         "MonicaFangirl87","RoyaalTtt","crashen_burn","ShopEmLove","ima_lil_galaxy","etucl","Kiroshima_kyoto","wrmalath","Starah","alphaintj","DefiantCrimGrad","AcadEnforcer","AlveenaDoll","Akshay_Webster","benjaminspak","CAyf7","savannahjfoley","RaymondGW","asoma_almalki","JoByars","BreezyGhadeerr","cassieerosman","ogjerseygirl","Starah99",
         "bftwblog","INTJwriter","Raoofalbrahim","TheRangerSteve","SafaAhmes","TammyJParadis","IntjDiary","aleazara","Angersaurus","franandersoni","brennazucca","theonelori","talesddc","intjofficial","AlveenaDoll","JoByars","LeonDolinar","ana_korena","AmandaSueHowell","PeterKennell","focusordie","TerraHoward","VaultedSkies","Sarah_E_Cupcake")

intp = c("MarshallTanaka","dmhco","INTPjared","INTPinfo","an_intp","INTPprobs","INTP_af","intpedia","Forechecker","M40A3Predator","David_McNair","evilsocket","saraholmesSTL","kyylestyyle",
         "williams_kiih","LittleMissINTP","NicTrades","Khelechy_OF","chuchuroon","Dez_7Prezzi","caleb721","MyPotnaB","nahwan313","INTP_Ramble","MTBI_I","MehINTP","kiriise","videosmusic","PhilosopherK1ng","Chem_E_Bruh","INTPnarcissist","amanda_leigh","UrbanEpicurious","AlexSchleber","INTP48","katiepegler","WichitaCindy","stefanwobben","Astralix",
         "unfilteredINTP","curious_intp","abbyjperry","ness_intp","khwrzmi","intuitiveINTP","intpclaire","alyrs","livingwithINTP","brittanynb_","tylersschuckman","LessAloof","intp221","goldclub24","tinypatron","amateria","zilberhere","RevitFur","TheDavidJohnson","SMCADMAN","hrtl","mfoxme","Dobbln","mandiero","attebury",
         "theChristophe","cascadian","BobbyTaylor","anklxbiter","saylenny","TimAndrewsHere","Elysa_Ng","MicheleSlawon","ShaneStraw","MelricMelnibone","theaquawoman","WombatGombac","tehcoder42","starkspectre","WilmsIsBoss","ladybird53","HBCoen","hugooconnor","Muh217","xskaltum","catboxjellyfish","nikkxothermic","burndive","KnightSomething","Ulfakundl")

entj = c("entj_probs","theRealENTJ","rezaprabowo","Siphi_Kuz","paulwrblanchard","ryanstruyk","DiageoLiam","TScholesFogg","zmh","kmattio","mgeheren","dohertyjf","eliransapir","danamuses",
         "AMPhillipsENTJ","kylereed","MayaElious","noelbellen","jtangoVC","jespern","daRealistNeisha","andretacuyan","momofmac","AdsmKelly","ValntinesDay","mcmullenforus","SammanC","KelByrd","KclSoriano","Mahek_MD","cch","JustJennaV","entj_ish","mjslabbert","S_Horv","DARLA_ROCKS","missmeg703","TheShanelleM","LouisCyprien",
         "Harvatin","uuizardry","LeeYount","DickTaylor","ARKing247","Sarah_Nicolas","alora","DaveStopher","JustinRFrench","Lola_rEVOLucion","AnneMarieSqueo","theQSLman","CarolynneAlex","scotteg","JerrellAltic","GHeaberlin","SurbhiBachhawat","joshuagoode","DavesNotHereYo","AnnaHargisEVV","johanalarsson","jimohagan","UXDJB","illmaticomo","edwardd",
         "GinaMMontgomery","AndryosDeSouza","MsAmyILo","AnalyticsPanda","TealWillingham","C_Handerhan","elisabeth_wang","TheUncleLou","JennyKCMO","MiddleUSA","KnightIntoDay","kukuhberg","IsThatJeff","sun_and_coffee","scotteg","JerrellAltic","GHeaberlin","SurbhiBachhawat","joshuagoode","DavesNotHereYo","AnnaHargisEVV","johanalarsson","jimohagan","illmaticomo","UXDJB")

entp = c("MissENTP","rainbobrain","GrahamBM","jimspellmanTV","ENTPMaroon","quirkyENTP","kevinlien","heygregr","TiKris","StuPflaum","KapEntp","Nessa_the_ENTP","Meandaenie","ENTPstruggs",
         "toast1985","alexisvandam","maneesh","Luke360","TheLastENTP","ChrisMHooker","mvminah","NatMakepeace","entp_","mpppg","Sean_Davis","CalWells","hollyhodson","thebunnyluz","colinmegill","jest1","eriiiic","CarolPinchefsky","bethanymarz","Steven_McKie","RajNijjer","rjnaguitskona","MelLohEntp","axlena_","djx_entp",
         "MalikFriendsEn1","deboone","RickBullotta","pa1ntbucket","Allstar_Entp","LeeTheENTP","NikhilMoreV","AnneRipley","jaysonwhelpley","LauraBQuigley","ARASHII_ENTP","paolojcruz","aeromati","denimgege","MilesNextDoor","jasonpemberton","NoelleMandell","jimkilohertz","LeBlondeLoL","sassandglitter","yungtartarsauce","StuffOlgaThinks","stephenmedawar","joshomen","NWsidhe",
         "TheJoshNeal","TBOJP","BKKRickLee","kailawhite","oysta","regineran7","_khalessi_","JoEgenolf","HealerJillo","ScottSBaker","TJWallace_","sgutier","PapemelroticPAT","dianeareyes","mssjr139","delcaliche","adik_apriliyadi","mscannjr","TY_FI","ej_white7","NofalAlmusarea","ConcertPictures","MO2AMIN","kjdeja","beadjunky18")

#######################################################
#Personality categories [Diplomats]
#######################################################

infj = c("hspinfj","idrobinhood","infjanonymous","ConfessionsINFJ","me_infj","idealistmuse","INFJ_Believer","INFJThinking","MadameAmbassK","JumbledCosmic","Infjmatt","ms_infj","Sil_Lai","nfjtheband",
         "LadyINFJ","battymamzelle","TheAlpacasaur","randominfj","AllTooEphemeral","sarahbessey","trueINFJ","INFJlife","INFJHere","INTJ_INFJ","scottsauls","protectinfj","starryinfj","Tramaine_C85","ourseventulips","catholic_nun","slicknet","fridaspies","MBTIxINFJ","Mindful__INFJ","litford","andrearosen","INFJme","DP_Dietrich","ALEC_EMPIRE",
         "TurtleKing4","TheBarracuda57","Jake_STweets","pyuric","Infj44","ruhanirabin","tresham","infjstruggles","theinfjmale","haileymow","MayotGabbi","INFJ13","Rinoaaa","dougieINFJ84","sable_swan","infj_advocate","mbticrap","KittyqueenB","RareOneINFJ","LifeOfAnINFJ","infj_stanley","InfjBooklover","JTanKewen","CapricornINFJ","CaptHat211",
         "jimcaviezelINFJ","INFJEyes","INFJ_Princess","phyllistoh","JohnBechard","Inspired_INFJ","BigWeirdCow","DrewsClues","Whitnage","ashbridgess","ivoryandgoId","LutfiHidayatR","ChristinaJuneYA","AndareVeloce","saragast","cary","EliseCaile","brandice","vSh0tGuNv","JarheadPAO","MattRosser","AnomaPaleebut","mel_allen","Hurmoth","ShivaShafii")

infp = c("infpprince","jamietworkowski","Uniquely_INFP","DisillusionedNF","bilbaobab","INFPprobs","Yoana81","MinaMarkham","whatsaroutine","ObsessedINFP","SANTINORICE","infpdiary","Rizubesuu","INFPMind",
         "mpolinar","Angelo_Mikha","INFP_Feels","jeongjk0","INFPerceptions","INFPInTears","INFPbrain","TheInfp","paoacflores","infpworld_","UmaINFP","sarahwhitmire","lyndsayj","BaeSooRa","adityadaniel","shayla_brooks","katiejrice","angryinfp","thisisyunqing","HiMyNameIsINFP","DIY28","ashnta","MirenxOTM","Keltounet","helleluyeah",
         "klassy","jenkwok","Jellydraws","infp_INKS","kosherjellyfish","biblio_phile","sadukie","INFP_Story","anotherschwab","CharCharPR","bunnyhaveadream","Jon_Sadler","TheCanadienne","MrPoonchee","Hydraslaught","octoberjuneblog","__blackwell__","RandallJohn","cardassianv0le","CarynCaldwell","Gandoora32","Court_Kae","kristizia","Li_Li_D","meadowssulli",
         "danieldessinger","nomadmanager","KaiCarra","Emily_Jeffords","KidTheCrash","zzuuu","badwlof","jacyoverstreet","MatthewBoulden","jobuch27","Hannahwarmisham","Ariel_meep","kikiverde","cactuswrenwrite","ohsosteffany","elisabetherin_","peaceandALLlife","SuCheese","joankaufman","MeeshUniVerSoul","PersonalWeirdo","sand_writer","sugargirlxox","DavePaterson","chendelier")

enfp = c("justenfp","siobhanvivian","nprobin","Enfpthatsme","hallstigerts","RyanArnoldRocks","wildbeauty","debontherocks","PascalGaroute","TheaAlberto","christinelu","ludwikc","tregp","jds_enfp",
         "JamesJWalsh","raghunotragu","KatieMcKiever","AccLeicsPolice","jmatthews1065","TheNoragami","danceyiqi","nlevin","ricklessabandon","PramathSinha","dawahaddict","StephanieFrasco","UpsideUp","Enfprelate","AlbertaShendy","Iolitadolly","jaydixit","SortaAwesomeMeg","andiana","JanetBoyer","smbourzac","sherrierohde","FreeRangeHumans","JGrantJenkins","DariaBurke",
         "tislaurapearson","DWKPhD","AdsmKelly","Neeka_Blake","DavidGoecke","PoppiesOfBlue","AmbiNFP_Bambi_","Curlsandwords","SavannahB","BellDomRussell","tikikate","spencerb","kevinforch","revizion","Kristin_Kepp","KyloKaren","NatalieJosh","jenhatzung","DavidArnoldCFB","HoekedOnPhonics","robinkurz","katielizg","ohjphan","ClaraBiznass","wininsley",
         "MsKristineAbbey","MishheKHT","BimAfrido26","kerri_brett","madisonkerr","brittomart","ashleygurule","SayCrunch","SelenaShines","charbrum","kayleeharwood","F_ScottinTexas","reydisutandang","DeliciouzDezine","giyaang","thealyoxales","kriscrittah","hoppimike","hillviewspecial","MRoboski","rzqikrniawan","2PMagreement2ll","dskyeung","denisaaa","booboojuri")

enfj = c("JarrettHill","mpesce","steenfox","sabikaamalina","b_shap","IzzyGould","InstantRHIplay","JMACdaKID","MKSuttonENFJ","starheal","SEOcopy","allysonrobinson","HeatherLBrady","alexialafata",
         "enfj_maria","asch_","_seeEmilyplay_","lunatic_enfj","revsusanrussell","LisaMParkin","Richard_Sink","icod","shannonsmedstad","akshat_rajan","AaronBrown_ENFJ","ejly","leahfaul","aggiemeesh","edaltonsmith","ayymanduh","Deezy2_Blessed","romanocog","ToddHellsKitch","torimccue_","ReneePrudhomme","CiLLASTAYFLY","su_nami_","tuneycorn","EvanTraylor",
         "berryemoji","lesliebriskman","j_nerdy_","kjaerglobal","RickyTM7","LoveASharie","c_gonzalez","MelissaJudy","Datification","sgro97","joestanley","joytea","linzpollard","OhMyJenniferZ","DorianeMouret","oakandoats","TrebahKM","eebell","anohsar","jonathan_yu","chaoskitten82","justinmunger","courtnycotten","simonaioffe","johnbcavanaugh",
         "titoindo","alesssia","MelRoc7","LolaSpeaking","AnnaInez_","patriciaco","MrsPersiemistic","ooodalishis","ust20percent","Laine_Mello","caitlinjena","jdepauw","TheSaifSide","ElizabethMKit","AniuPishu","FredBantados","RevDavidBowen","whitewolfangel7","BGreathouse","brenonkalu","Okhilleus","xd1936","BGdoitwell","POPaMOli","mamimangux")



#rmb not to use protected users, which are represented by a lock on their profile

##########################
#insert profile below:
profile = enfj
##########################

wordVector = rep("empty", length(profile))
for (i in 1:length(profile)){

result <- try(userTimeline(profile[i], n = 80, retryOnRateLimit=10));
if(class(result) == "try-error") next;  
tweet = result  
#tweet = userTimeline(profile[i], n = 80, retryOnRateLimit=10)
tweet = strip_retweets(tweet)

#userTest = userTimeline("ardydo", n = 1, retryOnRateLimit=10)

tweets_cl = tweet
tweets = sapply(tweets_cl,function(x) x$getText())
tweets_cl = gsub("(RT|via)((?:\\b\\W*@\\w+)+)","",tweets)
tweets_cl = gsub("http[^[:blank:]]+", "", tweets_cl)
tweets_cl = gsub("@\\w+", "", tweets_cl)
tweets_cl <- str_replace_all(tweets_cl,"#[a-z,A-Z]*","")
tweets_cl = gsub("[ \t]{2,}", "", tweets_cl)
tweets_cl = gsub("^\\s+|\\s+$", "", tweets_cl)
tweets_cl <- gsub('\\d+', '', tweets_cl)
tweets_cl = gsub("[[:punct:]]", " ", tweets_cl) 
tweets_cl = gsub("[^[:alnum:]]", " ", tweets_cl)
tweets_cl = tolower(tweets_cl)
words.list = str_split(tweets_cl, "\\s+")
# or str_split(tweets_cl, " ")

words = unlist(words.list)
words = words[words!="s"] #take out s from the tweet words
words = words[words!=""]
words = paste(words, collapse=" ")

wordVector[i] = words
}

##########################
#Save as ____Vector from wordVector
##########################

#save intj (87) wordVector as intjVector
intjVector = wordVector
wordVector = intjVector
words = wordVector

#save intp (89) wordVector as intjVector
intpVector = wordVector
wordVector = intpVector
words = wordVector

#save entj (89) wordVector as intjVector
entjVector = wordVector
wordVector = entjVector
words = wordVector

#save entp (89) wordVector as intjVector
entpVector = wordVector
wordVector = entpVector
words = wordVector

#save infj (89) wordVector as intjVector
infjVector = wordVector
wordVector = infjVector
words = wordVector

#save infp (89) wordVector as intjVector
infpVector = wordVector
wordVector = infpVector
words = wordVector

#save enfj (89) wordVector as intjVector
enfjVector = wordVector
wordVector = enfjVector
words = wordVector

#save enfp (89) wordVector as intjVector
enfpVector = wordVector
wordVector = enfpVector
words = wordVector

##################################################################
#Done so far (80)
################

#######################################################

wordVector = rep("empty", 89)
for (i in 1:87){ #loop to loop into the wordVector
wordVector[i] = words[i]
mbtiVector = rep("enfj", 89)

#for showing Shengs
diplomatVector = rep("diplomat", 89)
seeShengs = cbind(mbtiVector, diplomatVector, wordVector)
write.csv(seeShengs, file = "enfj.csv")
#if (!is.na(seeShengs)) row.names = NA
#analystVector = rep("enfj", "analyst", 1)
}

#######################################################
#Completed personality categories [Analysts]
#######################################################



#######################################################
#Completed personality categories [Diplomats]
#######################################################


#######################################################
#Sentiment Score Code
#######################################################

vector = rep(0,3)

for (i in 1:length(tweets)){
  pos.matches = match(words.list[[i]], ":)")
  neg.matches = match(words.list[[i]], ":(")
  
  pos.matches = sum(!is.na(match(words.list[[i]], ":)")))
  neg.matches = sum(!is.na(match(words.list[[i]], ":(")))
  
  score = pos.matches - neg.matches

  print(pos.matches)
  print(neg.matches)
  print(score)
  
  if (score == 0){
    vector[2] = vector[2] + 1
  }
  if(score > 0){
    vector[1] = vector[1] + 1
  }
  if(score < 0){
    vector[3] = vector[3] + 1
  }
}

print(vector)
#left side is no. of positive tweets, 
#middle is neutral, either no emojis or counteracted
#right is no. of negative tweets

#Converting tweets to a Dataframe format:
#df = twListToDF(tweets)
#write.csv(df, file = "df.csv") #write as a CSV file, storing it in your local directory.