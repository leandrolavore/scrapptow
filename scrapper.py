from selenium import webdriver
import os
from bs4 import BeautifulSoup as soup
import json


data = []


def scrap(containers):
    for container in containers:
        title_tag = container.find("b")
        try:
            title = title_tag.text
        except:
            title = "no title available"

        address_tag = container.find_all('div')

        try:
            address = address_tag[2].text
        except:
            address = "no address available"

        address_tag2 = container.find_all('div')
        try:
            address2 = address_tag2[3].text
        except:
            address2 = "no address available"

        phone_tag = container.find_all('div')
        print(phone_tag)
        try:
            phone = phone_tag[4].text
        except:
            phone = "no phone available"



        data.append({"title": title,
                     "address": address+', '+address2,
                     "phone": phone})
        with open("tow-scrap.json", "w") as writeJSON:
            json.dump(data, writeJSON, ensure_ascii=False)

url = os.environ.get('URL')

browser = webdriver.Chrome('C:\\Users\Leandro\Downloads\chromedriver.exe')
browser.get(url)

xml= """ 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"><head>
		<title>Your City Business Directory for Gold Coast, Queensland</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="keywords" content="Gold Coast, Tweed Heads, Coolangatta, Surfers Paradise, Nerang, Southport, Indy">
		<link rel="stylesheet" href="/yourcity1.css" content-type="text/css">
		<link rel="shortcut icon" href="/favicon.ico">
		<script src="https://pagead2.googlesyndication.com/pub-config/r20160913/ca-pub-8562565599145907.js"></script><script src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><script src="https://www.googletagservices.com/activeview/js/current/osd.js?cb=%2Fr20100101"></script><script src="https://pagead2.googlesyndication.com/pub-config/r20160913/ca-pub-8562565599145907.js"></script><script language="Javascript" src="/yourcity1.js"></script>
		<script language="Javascript"><!--
var city='14';
var current = new Date();
var starttime = current.valueOf() - 1562737910500;
if (document.getElementById) {
	document.write("<style type=\"text/css\"><!--\n.buslink, .membergallery, #catlist tr, .h, #catmenu td, #cityselect, #memberevents td, #featured, .callnk, .calev, .pro, .divlnk, .divlnkover {\ncursor: pointer; cursor: hand;\n}\n#pctable td input, .hide { display: none; }\n--></style>\n");
}
//--></script><style type="text/css"><!--
.buslink, .membergallery, #catlist tr, .h, #catmenu td, #cityselect, #memberevents td, #featured, .callnk, .calev, .pro, .divlnk, .divlnkover {
cursor: pointer; cursor: hand;
}
#pctable td input, .hide { display: none; }
--></style>

		<style type="text/css">
<!--
.style7 {font-size: 12px}
body {
	background-color: #C0C0C0;
}
-->
		</style>
	<link rel="preload" href="https://adservice.google.com.au/adsid/integrator.js?domain=www.yourcity.com.au" as="script"><script type="text/javascript" src="https://adservice.google.com.au/adsid/integrator.js?domain=www.yourcity.com.au"></script><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=www.yourcity.com.au" as="script"><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=www.yourcity.com.au"></script><link rel="preload" href="https://pagead2.googlesyndication.com/pagead/js/r20190708/r20190131/show_ads_impl.js" as="script"></head>
	<body>
		<center><table border="0" cellpadding="0" cellspacing="0" width="95%"><tbody><tr><td><table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#ffffff" id="header"><tbody><tr><td align="left"><table border="0" cellpadding="10" cellspacing="0"><tbody><tr><td valign="bottom" align="left" width="160"><a href="/cityselect.php?city=14"><img src="/images/hlogo.png" width="250" height="121" alt="Your City" border="0"></a></td><td valign="bottom" style="background: url(/images/header_bg.jpg) no-repeat bottom left" width="350"><div><span class="cname">gold coast</span><span class="cstate">queensland</span></div><div class="ctag">find, try &amp; buy local- Your Local Directory </div></td></tr></tbody></table></td>
		<td align="right" valign="bottom"><table border="0" cellpadding="10" cellspacing="0" id="cityimages"><tbody><tr><td><img src="/image.php?op=city&amp;id=14&amp;s=1" width="90" height="59"><img src="/image.php?op=city&amp;id=14&amp;s=2" width="90" height="59"><img src="/image.php?op=city&amp;id=14&amp;s=3" width="90" height="59"></td></tr></tbody></table></td></tr></tbody></table>
		<table border="0" cellpadding="0" cellspacing="0" width="100%" class="linkbar"><tbody><tr>
			<td align="left" width="240">
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wednesday 10th July 2019</td>
			<td align="left" id="timetick">5:02:29 pm</td>
			</tr></tbody></table>
		<table border="0" cellpadding="0" cellspacing="0" width="100%"><tbody><tr>
			<td width="205" valign="top" class="menu">
			
			<div id="citylights"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr>
			  <td height="30">&nbsp;</td></tr></tbody></table>
			</div>&nbsp;
			
			
			<div id="otherstate"><a href="/cityselect.php?city=14">Select a different State</a></div>
			<div id="cselect"><img src="/images/citysel.gif" width="32" height="50" alt="">
<form method="get" action="/index.php"><div>SEARCH A CITY</div><select size="1" name="city"><option value="13">Brisbane</option><option value="4">Cairns</option><option value="14" selected="selected">Gold Coast</option><option value="11">Hervey Bay</option><option value="7">Mackay</option><option value="31">Ravenshoe</option><option value="18">Sunshine Coast</option><option value="2">Townsville</option><option value="32">Whitsundays / Proserpine</option></select> <input type="submit" value="Go"></form></div>
			<div>&nbsp;</div>
			<center><img src="/images/categoryhead.gif" width="192" height="22" alt=""></center>
			<div>&nbsp;</div>
			<table border="0" cellpadding="0" cellspacing="0" width="205" id="catmenu">
<tbody><tr><td align="left" cid="1"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/1">Accommodation</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="60"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/60">Attractions</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="125"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/125">Baby</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="35"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/35">Building &amp; Renovation</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="31"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/31">Business Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="55"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/55">Clubs &amp; Groups</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="321"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/321">Communications</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="21"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/21">Computers</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="153"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/153">Emergencies</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="136"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/136">Employ/Education/Training</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="714"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/714">Entertainment</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="48"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/48">Family Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="113"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/113">Fashion &amp; Accessories</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="32"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/32">Financial Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="135"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/135">Florists</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="118"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/118">Food &amp; Liquor</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="433"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/433">Government Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="37"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/37">Health &amp; Beauty</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="737"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/737">Hotels /Pubs</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="116"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/116">House &amp; Garden</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="219"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/219">Industrial</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="3"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/3">Internet &amp; Online Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="107"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/107">Legal Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="127"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/127">Lifestyle</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="385"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/385">Manufacturers</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="42"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/42">Medical / Dental / Optical</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="62"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/62">Motor Vehicles</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="130"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/130">Occasions &amp; Functions</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="724"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/724">Office</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="108"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/108">Pets &amp; Pet Care</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="214"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/214">Photography</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="126"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/126">Real Estate</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="2"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/2">Restaurants / Dining</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="199"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/199">Security / Fire Services</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="154"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/154">Shopping Centres</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="189"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/189">Sports</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="192"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/192">Transport &amp; Storage</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="128"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/128">Travel</a></td></tr></tbody></table></td></tr><tr><td align="left" cid="327"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td><img src="/images/tc.gif" border="0" width="14" height="14"></td><td><a href="http://www.yourcity.com.au/cat/14/327">Wholesalers</a></td></tr></tbody></table></td></tr>			</tbody></table>
			<div>&nbsp;</div>
			<div align="center"><a href="http://www.ubiquitishop.com.au" target="_blank"><img src="/images/advertising/ubiquitishop-banner-yourcity.png" width="180" height="481" border="0" alt="More details here"></a></div>
		</td><td class="content" valign="top" align="left">
				<table border="0" cellpadding="0" cellspacing="0" id="headmenu" height="21"><tbody><tr><td align="right" width="11">&nbsp;</td>
		<td class="i0"><a href="/cat/14/"><nobr>home</nobr></a></td>
		<td class="i2"><a href="/about.php?city=14"><nobr>about us</nobr></a></td>
		<td class="i1"><a href="/join.php?city=14"><nobr>join FREE</nobr></a></td>
		<td class="i2"><a href="/contact_us.php?city=14"><nobr>contact us</nobr></a></td>
<td class="i1"><a href="/vouchers.php?city=14&amp;cat=0"><nobr>vouchers</nobr></a></td>
<td class="i2"><a href="/events.php?city=14"><nobr>events</nobr></a></td>
		<td class="i1"><a href="/support.php?city=14"><nobr>support</nobr></a></td>
		<td class="i2"><a href="/memberarea.php?city=14" style="padding-right: 1px"><nobr>login</nobr></a></td><td><a href="/memberarea.php?city=14"><img src="/images/greenend.gif" width="8" height="21" alt="]" border="0"></a></td>
		</tr></tbody></table>
		<table border="0" cellpadding="0" cellspacing="0" width="100%">
			<tbody><tr><td width="11"><img src="/images/view1.gif" width="11" height="11" alt=""></td><td background="/images/view2.gif"><img src="/images/view2.gif" width="20" height="11" alt=""></td><td width="11"><img src="/images/view3.gif" width="11" height="11" alt=""></td></tr>
			<tr><td background="/images/view4.gif">&nbsp;</td><td>
		<div class="quickfind">
		<div class="box">
			<h1>QUICK FIND</h1>
			<form method="get" action="/index.php">
			<table border="0" cellpadding="0" cellspacing="10">
				<tbody><tr>
					<td><b>FIND</b><br><span>(Business, Product, Service or Keyword)</span><br><input type="text" name="search" id="search" value="towing"></td>
					<td><b>IN</b><br><span>(State, City, Suburb or Postcode)</span><br><input type="text" name="location" id="location" value="Gold Coast"><br><label for="surround"><input type="checkbox" id="surround" name="surround">Include surrounding suburbs</label></td>
					<td style="vertical-align: middle"><input type="image" src="/images/findnow.gif" width="195" height="31" alt="Find Now"></td>
				</tr>
			</tbody></table>
			<input type="hidden" name="city" value="14">
			</form>
		</div>
</div><table border="0" cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td valign="top"><h2>Search for 'towing'</h2><div class="expired1"><div>&nbsp;</div><div><b>Aaa Allstate 24 Hour Towing</b></div><div>21 Ruth Terrace </div><div>Oxenford 4210</div><div>Ph: 0418 763213</div><div><a href="/details/13742" target="_blank" onclick="return busopen('13742', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Aaallstate 24 Hour Towing</b></div><div>21 Ruth Terrace </div><div>Oxenford 4210</div><div>Ph: 07 55974822</div><div><a href="/details/13790" target="_blank" onclick="return busopen('13790', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Aarons Discount Towing</b></div><div>81 Sharton Avenue </div><div>Buccan 4207</div><div>Ph: 07 38051211</div><div><a href="/details/13813" target="_blank" onclick="return busopen('13813', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/62">Motor Vehicles</a> ► <a href="/cat/14/69">Repairs &amp; Maintenance</a> ► <a href="/cat/14/268">Smash Repairs</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Archers Towing</b></div><div>9 United Road </div><div>Ashmore 4214</div><div>Ph: 0411 225559</div><div><a href="/details/14941" target="_blank" onclick="return busopen('14941', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Arthurs Towing Tilt Tray Hire</b></div><div>PO Box 175 </div><div>Ormeau 4208</div><div>Ph: 07 33820496</div><div><a href="/details/15020" target="_blank" onclick="return busopen('15020', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Beenleigh Towing</b></div><div>17 Thorsborne Street </div><div>Beenleigh 4207</div><div>Ph: 07 38073777</div><div><a href="/details/16217" target="_blank" onclick="return busopen('16217', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Bingles Towing</b></div><div>145 Rio Vista Boulevard </div><div>Broadbeach 4218</div><div>Ph: 0412 777009</div><div><a href="/details/16499" target="_blank" onclick="return busopen('16499', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Broadbeach Towing</b></div><div>145 Rio Vista Boulevard </div><div>Broadbeach 4218</div><div>Ph: 0412 777009</div><div><a href="/details/17005" target="_blank" onclick="return busopen('17005', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Cat Towing</b></div><div>2 Tralee Road </div><div>Eagleby 4207</div><div>Ph: 0403 185575</div><div><a href="/details/17837" target="_blank" onclick="return busopen('17837', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Cheaper Towing</b></div><div>Ivan Street </div><div>Labrador 4215</div><div>Ph: 0414 557161</div><div><a href="/details/18033" target="_blank" onclick="return busopen('18033', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div>&nbsp;</div>
<center>
<script type="text/javascript"><!--
google_ad_client = "pub-8562565599145907";
/* Yourcity Listing Banner 1 */
google_ad_slot = "5841985834";
google_ad_width = 468;
google_ad_height = 60;
//--></script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script><ins id="aswift_0_expand" style="display:inline-table;border:none;height:60px;margin:0;padding:0;position:relative;visibility:visible;width:468px;background-color:transparent;" data-ad-slot="5841985834"><ins id="aswift_0_anchor" style="display:block;border:none;height:60px;margin:0;padding:0;position:relative;visibility:visible;width:468px;background-color:transparent;"><iframe width="468" height="60" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0px;width:468px;height:60px;"></iframe></ins></ins>
</center>
<div>&nbsp;</div>
<div class="expired1"><div>&nbsp;</div><div><b>Club Towing</b></div><div>34 Bailey Crescent </div><div>Southport 4215</div><div>Ph: 07 55710799</div><div><a href="/details/18374" target="_blank" onclick="return busopen('18374', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Club Towing Services</b></div><div>34 Bailey Crescent </div><div>Southport 4215</div><div>Ph: 07 55710799</div><div><a href="/details/18375" target="_blank" onclick="return busopen('18375', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Garrards Transport Service G T S Towing</b></div><div>4 Glenmore Drive </div><div>Ashmore 4214</div><div>Ph: 0411 719205</div><div><a href="/details/21726" target="_blank" onclick="return busopen('21726', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Gold Coast &amp; Hinterland Towing Network</b></div><div>15 Price Street </div><div>Nerang 4211</div><div>Ph: 07 55961729</div><div><a href="/details/22039" target="_blank" onclick="return busopen('22039', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Gold Coast Emergency Towing Service</b></div><div>14 Strathaird Road </div><div>Bundall 4217</div><div>Ph: 0412 769583</div><div><a href="/details/22177" target="_blank" onclick="return busopen('22177', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Gold Coast Towing</b></div><div>10 Bronte Court </div><div>Robina 4226</div><div>Ph: 07 55930418</div><div><a href="/details/22442" target="_blank" onclick="return busopen('22442', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Harveys Towing Service</b></div><div>199 Alexandra Drive </div><div>Nerang 4211</div><div>Ph: 07 55273086</div><div><a href="/details/23077" target="_blank" onclick="return busopen('23077', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Helensvale Towing</b></div><div>50 Siganto Drive </div><div>Oxenford 4210</div><div>Ph: 0418 767151</div><div><a href="/details/23242" target="_blank" onclick="return busopen('23242', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><div class="expired1"><div>&nbsp;</div><div><b>Higgsys Heavy Towing &amp; Salvage</b></div><div>138 Castle Hill Drive </div><div>Gaven 4211</div><div>Ph: 0408 754575</div><div><a href="/details/23321" target="_blank" onclick="return busopen('23321', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/62">Motor Vehicles</a> ► <a href="/cat/14/69">Repairs &amp; Maintenance</a> ► <a href="/cat/14/268">Smash Repairs</a></span></div></div><div class="expired0"><div>&nbsp;</div><div><b>Hilla Towing Services</b></div><div>93 Spans Street </div><div>Beenleigh 4207</div><div>Ph: 07 38046535</div><div><a href="/details/23347" target="_blank" onclick="return busopen('23347', 680, 500)">Details + Map</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/memberarea.php">Edit</a><span class="loc"><a href="/cat/14/192">Transport &amp; Storage</a> ► <a href="/cat/14/196">Removalists</a></span></div></div><center><table border="0" cellpadding="0" cellspacing="1" class="pages"><tbody><tr><td>Page 1 of 3&nbsp;</td><td><a href="?page=1&amp;search=towing&amp;location=Gold Coast&amp;city=14" class="c">1</a></td><td><a href="?page=2&amp;search=towing&amp;location=Gold Coast&amp;city=14">2</a></td><td><a href="?page=3&amp;search=towing&amp;location=Gold Coast&amp;city=14">3</a></td></tr></tbody></table></center>			</td><td width="10"></td><td valign="top" width="160">&nbsp;<br><script type="text/javascript"><!--
google_ad_client = "pub-8562565599145907";
/* Yourcity R/Side Listings 160x600 */
google_ad_slot = "6562460688";
google_ad_width = 160;
google_ad_height = 600;
//--></script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</td></tr></tbody></table>
	<div>&nbsp;</div>
	<div style="text-align:center"><script type="text/javascript"><!--
google_ad_client = "pub-8562565599145907";
/* Yourcity Banner Listing Bottom 468 x 60 */
google_ad_slot = "9980350083";
google_ad_width = 468;
google_ad_height = 60;
//--></script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script><ins id="aswift_1_expand" style="display:inline-table;border:none;height:60px;margin:0;padding:0;position:relative;visibility:visible;width:468px;background-color:transparent;" data-ad-slot="9980350083"><ins id="aswift_1_anchor" style="display:block;border:none;height:60px;margin:0;padding:0;position:relative;visibility:visible;width:468px;background-color:transparent;"><iframe width="468" height="60" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0px;width:468px;height:60px;"></iframe></ins></ins></div>
	<div>&nbsp;</div>
	<div class="catadd">Add your business <span class="free">FREE</span> in yourcity, it's the place to be!!</div>
	<div>&nbsp;</div>
	<div><a href="/join.php?city=14&amp;category=">ADD YOUR BUSINESS HERE</a></div>

			</td><td background="/images/view6.gif">&nbsp;</td></tr>
			<tr><td width="11"><img src="/images/view7.gif" width="11" height="11" alt=""></td><td background="/images/view8.gif"><img src="/images/view8.gif" width="20" height="11" alt=""></td><td width="11"><img src="/images/view9.gif" width="11" height="11" alt=""></td></tr></tbody></table>
		</td></tr></tbody></table>
		<table border="0" cellpadding="0" cellspacing="0" width="100%" class="linkbar" height="20"><tbody><tr><td align="center"><a href="#">Top of Page</a> | <a href="/">Home</a> | <a href="/about.php">About Us</a> | <a href="/careers.php">Careers</a> | <a href="/join.php">Join Free</a> | <a href="/contact_us.php">Contact Us</a> | <a href="/vouchers.php?city=14&amp;cat=0">Vouchers</a> | <a href="/support.php">Support</a> | <a href="/memberarea.php">Login</a></td></tr></tbody></table></td></tr></tbody></table></center>
		<div align="center"><span class="style6"><span>©</span> 2019 <span class="style7">Your City, A division of Choice IT - All rights reserved</span></span></div>
		<script language="Javascript"><!--
initbus();
timetick();
initcatmenu();
//--></script>
	

<iframe id="google_osd_static_frame_5866890855915" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe><ins class="adsbygoogle adsbygoogle-noablate" style="display: none !important;" data-adsbygoogle-status="done"><ins id="aswift_2_expand" style="display:inline-table;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><ins id="aswift_2_anchor" style="display:block;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><iframe frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" onload="var i=this.id,s=window.google_iframe_oncopy,H=s&amp;&amp;s.handlers,h=H&amp;&amp;H[i],w=this.contentWindow,d;try{d=w.document}catch(e){}if(h&amp;&amp;d&amp;&amp;(!d.body||!d.body.firstChild)){if(h.call){setTimeout(h,0)}else if(h.match){try{h=s.upd(h,i)}catch(e){}w.location.replace(h)}}" id="aswift_2" name="aswift_2" style="left:0;position:absolute;top:0;border:0px;width:0px;height:0px;"></iframe></ins></ins></ins></body><iframe id="google_shimpl" style="display: none;"></iframe><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20190708/r20190131/zrt_lookup.html#" data-ad-client="ca-pub-8562565599145907" style="display: none;"></iframe></html>
"""

html_soup = soup(xml, "lxml-xml")
browser.maximize_window()

containers = html_soup.findAll("div", class_="expired0")
scrap(containers)
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired1")
scrap(containers)
browser.implicitly_wait(5)
browser.find_element_by_link_text("2").click()
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired0")
scrap(containers)
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired1")
scrap(containers)
browser.implicitly_wait(5)
browser.find_element_by_link_text("3").click()
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired0")
scrap(containers)
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired1")
scrap(containers)
browser.implicitly_wait(5)
browser.find_element_by_link_text("4").click()
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired0")
scrap(containers)
browser.implicitly_wait(5)
containers = html_soup.findAll("div", class_="expired1")
