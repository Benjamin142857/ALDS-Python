DOWN_TYPE = '#tab-g0-MP4';    // g-第几季对应顺序，注意修改,还有（HR-HDTV，MP4）
SOURCE = 1;     // 电炉、磁力...

$links = $(DOWN_TYPE + ' .down-list .item .down-links');
var ret = '';
for(var i=0; i < $links.length; i++) {
    var path = $($($links[i]).children()[SOURCE]).find('a').attr('href');
    ret += '[' + (i+1).toString() + ']' + '(' + path + ')\t';
}
console.log(ret);