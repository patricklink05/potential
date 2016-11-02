import math
import pvutil
import subprocess
import numpy as np 
k = 9 * 10 ** 9
q = 1
class epot(object):
	def __init__(self,r,pos,neg,qplus,qneg):
		self.r = r
		self.pos = pos
		self.neg = neg
		self.qplus = qplus
		self.qneg = qneg
		self.rpos = r - pos
		self.rneg = r - neg
		self.vpos = k * qplus / np.linalg.norm(self.rpos)
		self.vneg = k * qneg / np.linalg.norm(self.rneg)
		self.vtotal = self.vpos + self.vneg
r = np.array([[10],[0],[0]])
neg = np.array([[-1],[0],[0]])
pos = np.array([[1],[1],[1]])
r1 = epot(r,pos,neg,1,-1)
print r1.vtotal
testlist = [1,2,3]
contourdict = {}
contourdict[r1.vtotal] = r.tolist()
print contourdict



def equipot(pos,neg,qplus,qneg,amount):
	#the point of amount is to be a list of r values that you can check the potential at
	#a good way of doing this might be to use the sphere functions and evaluate potential at 
	#each point then continue
	listpots = []

	for r in amount:

		temphold = epot(r,pos,neg,qplus,qneg)
		phi = temphold.vtotal * .1
		if [True for item in listpots if temphold.vtotal + phi > item > temphold.vtotal - phi]:
			item + temphold.vtotal
			str(temphold.vtotal).append()
		else:
			listpots.append(temphold.vtotal)
			str(temphold.vtotal) = []
testhold = [[0.8715179993720135, 0.35229298579918805, 0.35480931802405224], [-3.1384793521392504, -0.2535528131017424, 0.4309419577718012], [-2.4516863655467223, 0.3309551256758021, 0.37479154844915336], [0.460603860708507, -0.49076852191075176, 0.09563607008621797], [-1.7631370363836067, -0.3812992718365711, 0.3234360296826881], [-3.461674850943024, -0.307996367025952, 0.39387591688095763], [-2.8561256097125636, -0.35926155650808617, -0.34775154063697145], [-0.7932630370517391, 0.010130310919161396, -0.49989736626699793], [0.7340546962293866, 0.011948130322324542, -0.4998572217961852], [-2.5687336051240557, -0.40046790219713535, -0.29937511471367434], [0.377538345580394, -0.07863338628403563, 0.49377807825125813], [1.3371686690079416, -0.41528194275433367, -0.278461681425266], [1.2462445143324192, 0.4939576021229597, -0.07749765999651798], [0.7730329311791557, -0.42485039244322964, -0.26363259290314195], [1.7685610482048721, 0.46832453476426805, 0.17513460576891118], [0.7014962142780403, 0.4467126521215226, -0.22460589136208234], [-2.3291789232031475, -0.43106769262979244, 0.25333899101959567], [1.1173282010873518, -0.34956240619005147, 0.3574998240260007], [2.059163693707794, 0.31707629455062264, -0.3866039619999345], [3.3493243375549238, -0.46661375694687995, 0.17964298435485332], [-3.4880896513285293, -0.3630086124047284, 0.3438382574990655], [3.4963291755677215, 0.3380730559703266, 0.36838377926679183], [2.1760527571640473, 0.28989264801957654, 0.4073846494704948], [3.5066475337007255, -0.25320757396514487, -0.43114489964127567], [2.3926064364078297, -0.48472573424632864, -0.12264160207432723], [3.4707323120332854, -0.05830161127442344, -0.4965892891744706], [-1.9860717699356796, 0.39920846269138177, -0.30105249262476413], [-1.5883006313690275, 0.49812900444828984, 0.04321452218127253], [0.9180097163398884, 0.2215424435989964, -0.448239830541849], [3.084527268684635, 0.36492560608687064, 0.3418030164029132], [-3.360910411154415, -0.295616588575768, 0.40325033485271294], [3.292725212213517, -0.29878388985531307, 0.4009092006463909], [-2.225830599590595, -0.39366980615299774, 0.30825976663110155], [1.7778202867360884, -0.4175488024244921, 0.27505090000556714], [-1.651217729851182, 0.08540618783049544, -0.4926517868436712], [-1.708916328358546, -0.4981245191567368, -0.04326619251644203], [1.4366289433446777, -0.483173927276024, 0.12861942310811192], [-3.199898655126841, -0.4031558327425827, -0.29574545562972676], [3.7790553102780793, 0.4146587049679658, 0.279388901702071], [3.920327493860386, -0.005749639939406319, 0.49996694054763974], [-0.7551745416494917, 0.46510629520681795, -0.1835105832342876], [-3.0171854713480863, 0.1874925921904577, 0.4635154019811021], [-3.842831882219852, -0.47636827339737675, 0.1518988745856999], [-1.3262996092500678, 0.30054221644244855, -0.3995927628672226], [0.6752125736387349, -0.21708274190395838, 0.4504165662666721], [-3.97046429184127, -0.43176139780055084, 0.25215490352026565], [-3.0311160175324137, 0.4789276584715426, -0.14362554769596342], [-1.0864770951169156, 0.4129522687622153, 0.281904990598143], [2.5101719231387385, -0.35066341339718854, 0.3564199356161667], [0.3537872127470534, 0.3759000430582127, -0.3296955529406393], [3.3095909774543335, 0.37946317175358324, 0.3255882388580868], [-3.2680853120643176, 0.4824350278772012, 0.1313637844960479], [0.768344819233377, -0.020482375077253697, -0.49958029615988125], [-3.3924738160820125, -0.4999401916926846, -0.007733351814175843], [1.011764821101619, -0.4802580611063262, -0.1391121660473746], [0.06559202547945109, -0.28997025284427747, 0.4073294151733039], [3.6485125298391514, -0.4976591821155488, -0.04832533968926692], [0.2011815394304497, -0.49914270766076996, -0.029267001709693062], [3.3445093484774375, 0.01053653754830082, -0.499888969048621], [-0.07703357013615264, 0.0011909394228106413, -0.4999985816612795], [-0.31390197143914644, -0.24436487266293758, -0.43621761657276786], [2.8308447755176545, -0.22985687286076326, 0.4440335775576786], [-0.6860567895082772, 0.03413555016851706, -0.49883340326675457], [1.6197486327436925, 0.395779250835099, -0.305546697917696], [-1.534577471108583, 0.29911901671647156, -0.4006592240777332], [3.1137546395586986, 0.46995204591049916, 0.17071928580138845], [2.18084498911628, 0.3364586606589054, 0.3698588510061853], [-3.0701000349653036, -0.32766593231142105, -0.37767054002461886], [2.1961884633624322, 0.15182017753770638, -0.47639336025223866], [1.44048656506929, 0.41563875631988445, -0.2779288114695195], [0.7934631614903429, 0.2484235916544174, 0.4339190236778278], [-1.8357369333340587, 0.3597611549062699, 0.34723466333375597], [2.3127198785185614, 0.0737307541538344, -0.4945338976166414], [2.285016784745337, 0.4511567747973507, -0.21554016923639208], [2.772735110980748, -0.4953730359497478, 0.06786424134940232], [-0.09451198162842633, -0.0011525698075992889, 0.49999867158107386], [-0.7472216381302221, 0.22227513255167133, -0.44787695346951817], [-3.5794374403384897, -0.27476968915691946, 0.41773390803310406], [-3.191410543646964, -0.2862728403839644, 0.4099364107498835], [-1.1608509813895527, 0.4999195589462505, 0.008968532933898609], [0.16023726188469478, 0.4851797318328054, 0.12083305764006425], [-2.08812920253241, 0.3742372323413729, 0.3315818057877562], [2.948855919610356, -0.3618250558859716, -0.3450835100857668], [-2.3915795122695807, -0.29113416223899136, -0.40649833896019877], [0.08679264963863442, -0.39161816471451416, -0.3108620482877182], [3.9490969663205027, 0.49148611124480435, -0.09187710516477901], [3.773975820328717, 0.24805658792362753, -0.43412893152574805], [0.902536273263606, -0.44294750205797606, 0.2319429033633047], [-2.4034149511830822, -0.49995301767645617, -0.006854204272208869], [0.6543599116985135, 0.4042691619844463, -0.2942217610381556], [-3.905701149296073, -0.14293895325955083, -0.4791330249952135], [0.5947519892701205, 0.4638633198106634, -0.18663017048224073], [3.762478290643579, -0.03185275857245308, -0.4989843702675716], [3.436725807070851, -0.2970022911860211, -0.40223082804560606], [2.066948378869487, -0.4252496423479295, 0.262988101789716], [0.38868486464133767, -0.49682951960790744, -0.05621768801877204], [-3.1137078843707657, 0.27605247072605144, -0.41688731499776116], [2.38646359404083, 0.13339979066451466, -0.4818760170942974], [0.035721879925455724, 0.3118430862505323, -0.39083742087694606], [1.7309793638406283, 0.3389782677037409, 0.36755099513478534], [3.9999999999999996, 0.31830346004952387, -0.23008742817338385], [-3.9999999999999996, -0.2940348184811725, 0.393892688570541], [3.9999999999999996, -0.23365520440841556, 0.05045489088170186], [3.9999999999999996, 0.32176086983679614, -0.14385242241814228], [-3.9999999999999996, -0.0756898615585174, 0.024036811566656414], [3.9999999999999996, 0.06226065642967474, -0.05810847923925115], [3.9999999999999996, -0.04421843089396246, -0.07529650413031976], [3.9999999999999996, -0.33853861875060387, -0.04383013680574467], [-3.9999999999999996, -0.08581782483459927, 0.04360892200019537], [-3.9999999999999996, -0.25237010891576017, -0.41617007117581434], [-3.9999999999999996, -0.2447062691592731, -0.42061068741098345], [-3.9999999999999996, 0.101601599994345, -0.22414055412866796], [-3.9999999999999996, -0.17636429660824438, -0.18422292248789052]]
equipot(pos,neg,1,-1,testhold)
