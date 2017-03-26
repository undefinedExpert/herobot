import re

from bs4 import BeautifulSoup


data = """
<script type="text/javascript">$(document).ready(function(){jQuery.fn.anim_progressbar=function(aOpts){var iCms=1000;var iMms=60*iCms;var iHms=3600*iCms;var iDms=24*3600*iCms;var vPb=this;return this.each(function(){var iDuration=aOpts.finish-aOpts.start;$(vPb).children('.pbar').progressbar();var vInterval=setInterval(function(){var iLeftMs=aOpts.finish-new Date();var iElapsedMs=new Date()-aOpts.start,iDays=parseInt(iLeftMs/iDms),iHours=parseInt((iLeftMs-(iDays*iDms))/iHms),iMin=parseInt((iLeftMs-(iDays*iDms)-(iHours*iHms))/iMms),iSec=parseInt((iLeftMs-(iDays*iDms)-(iMin*iMms)-(iHours*iHms))/iCms),iPerc=(iElapsedMs>0)?iElapsedMs/iDuration*100:0;$(vPb).children('.percent').html('<b>'+iPerc.toFixed(1)+'%</b>');$(vPb).children('.elapsed').html(iHours+'h:'+iMin+'m:'+iSec+'s</b>');$(vPb).children('.pbar').children('.ui-progressbar-value').css('width',iPerc+'%');if(iPerc>=100){clearInterval(vInterval);$(vPb).children('.percent').html('<b>100%</b>');$(vPb).children('.elapsed').html('<b>Finished</b>');if(aOpts.loaded){document.getElementById('complete'+aOpts.id).innerHTML='<form action="" method="GET"><input type="hidden" name="pid" value="'+aOpts.id+'"><input type="submit" class="btn btn-mini" value="Complete"></form>';}}else{}},aOpts.interval);});}
var iNow=new Date().setTime(new Date().getTime()-1);var iEnd=new Date().setTime(new Date().getTime()+8388*1000);$('#process32957275').anim_progressbar({start:iNow,finish:iEnd,interval:100,id:32957275,loaded:true});var iEnd=new Date().setTime(new Date().getTime()+5430*1000);$('#process32957276').anim_progressbar({start:iNow,finish:iEnd,interval:100,id:32957276,loaded:true});var iEnd=new Date().setTime(new Date().getTime()+0*1000);$('#process32957269').anim_progressbar({start:iNow,finish:iEnd,interval:100,id:32957269,loaded:false});});</script>
"""

# data = """T<script> TESTING CHUJU test TESTING</script>"""

# Date().getTime()+8388*1000);$('#process32957275') - looking for

# pattern = re.compile(r'\.val\("([^@]+@[^@]+\.[^@]+)"\);', re.MULTILINE | re.DOTALL)
# pattern = re.compile(r'_x\d+_y\d+\.npy', re.MULTILINE | re.DOTALL)



string = 'process32957275'
string_end = "Date().getTime()+8388*1000);$('#process32957275')"
# pattern = re.compile('(?:Date)', re.MULTILINE | re.DOTALL)

# process_id = 'process32957275'
# pattern = re.compile(r"Date\(\).getTime\(\)\+\d{0,4}\*\d{0,4}\)\;\$\('#" + process_id + "'\)", re.MULTILINE | re.DOTALL)

process_id = 'process32957275'

pattern = re.compile(r"Date\(\).getTime\(\)\+\d{0,4}\*\d{0,4}\)\;\$\('#" + process_id + "'\)", re.MULTILINE | re.DOTALL)
time_pattern = re.compile(r"\d{0,4}\*\d{0,4}")

soup = BeautifulSoup(data, "html.parser")

script = soup.find("script", text=pattern)
# print(script)

if script:
    # match = pattern.search(script.text)
    matched_all = re.search(pattern, script.text)
    time = re.search(time_pattern, matched_all.group(0))
    # finded_all = re.findall(pattern, script.text)
    if matched_all:
        time_cutted = time.group(0)
        print('')
        print(time_cutted)
