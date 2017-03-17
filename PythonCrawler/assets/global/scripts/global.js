// 全局定义method
Function.prototype.method = function(name,func){
	this.prototype[name] = func;
	return this;
};
	
// 核心脚本 控制整个主题和核心功能
// 为什么以这种形式书写：
// 	因为 JS 的作用域问题（函数作用域），为了实现某个功能又不想污染全局变量，会使用这种自执行的匿名函数。

// 这种形式书写的好处：
// 	1.这段代码被载入时自动执行；
// 	2.避免污染全局变量

// 还有其他什么这种类似的形式：
// 	1.(function() { /* code */ })();
	


// 一  问题引入：

// 	一般看JQuery插件里的写法是这样的
// 		(function($) {         
// 		  //...  
// 		})(jQuery);

// 	今天看到bootstrap的javascript组件是这样写的
// 		!function( $ ){
// 		  //...
// 		}( window.jQuery );
// 	为什么要在前面加一个 " ! " 呢？


// 二  问题解答：
	// 我们都知道，函数的声明方式有这两种
		// function fnA(){alert('msg');}			//声明式定义函数
		// var fnB = function(){alert('msg');}		//函数赋值表达式定义函数

	// 通常，我们调用一个方法的方式就是 FunctionName()。
	// 但是，如果我们尝试为一个“定义函数”末尾加上()，解析器是无法理解的。
		// function msg(){
		//   alert('message');
		// }();//解析器是无法理解的

	// 定义函数的调用方式应该是 msg() ; 那为什么将函数体部分用()包裹起来就可以了呢？

	// 原来，使用括号包裹定义函数体，解析器将会以函数表达式的方式去调用定义函数。
	// 也就是说，任何能将函数变成一个函数表达式的作法，都可以使解析器正确的调用定义函数。而 ! 就是其中一个，而 + - || 都有这样的功能。
	// 另外，用 ! 可能更多的是一个习惯问题，不同的运算符，性能是不同的。
	//结论是有意义的：括号和加减号最优，new方法永远最慢。结论来源：http://swordair.com/function-and-exclamation-mark/


// 最后：
// 	深入理解JavaScript系列（3）：全面解析Module模式
// 	http://www.cnblogs.com/TomXu/archive/2011/12/30/2288372.html




var Snail = function(){

	//IE mode
	var isRTL = false;
	var isIE8 = false;
	var isIE9 = false;
	var isIE10 = false;

	var resizeHandlers = [];
	var assetsPath = '../../assets/';
	var globalImgPath = 'global/img/';
	var globalPluginsPath = 'global/plugins/';
	var globalCssPath = 'global/css/';

	//主题颜色
	var brandColors = {
        'blue': '#89C4F4',
        'red': '#F3565D',
        'green': '#1bbc9b',
        'purple': '#9b59b6',
        'grey': '#95a5a6',
        'yellow': '#F8CB00'
	};

	//初始化主要设置
	var handleInit = function(){
		if ($('body').css('direction') === 'rtl') {
			isRTL = true;
		}

		isIE8 = !!navigator.userAgent.match(/MSIE 8.0/);
		isIE9 = !!navigator.userAgent.match(/MSIE 9.0/);
		isIE10 = !!navigator.userAgent.match(/MSIE 10.0/);

		if(isIE10){
			$('html').addClass('ie10');
		}

		if (isIE10 || isIE9 || isIE8) {
			$('html').addClass('ie');
		}
	};

	//运行回调函数
	var _runResizeHandlers = function(){
		for (var i = 0; i < resizeHandlers.length; i++) {
			var each = resizeHandlers[i];
			each.call();
		};
	};

	//根据窗口大小 布局初始化
	var handleOnResize = function(){
		var resize;
		if (isIE8) {
			var currheight;

			// jQuery 事件 - resize() 方法
			// 当调整浏览器窗口的大小时，发生 resize 事件。
			// resize() 方法触发 resize 事件，或规定当发生 resize 事件时运行的函数。

			//clientHeight 窗口大小
			// 跨浏览器确定窗口的大小并不是一件简单的事儿。IE9+、Firefox、Safri、Opera和Chrome均为此提供了四个
			// 属性：innerWidth、innerHeight、outerWidth和outerHeight。在IE9+、、Firefox、Safri中，outerWidth和outerHeight
			// 返回浏览器窗口本身的尺寸（无论是从最外层的window对象还是某个框架访问）。在Opera中，这两个属性的值表示页面视图
			// 容器的大小。而innerWidth、innerHeight则表示该容器中页面视图区的大小（减去边框宽度）。在Chrome中，outerWidth和
			// outerHeight与innerWidth、innerHeight返回相同的值，即视口(viewport)大小而非浏览器窗口大小。

			// IE8及更早版本没有提供取得当前浏览器窗口尺寸的属性；不过它通过DOM提供了页面可见区域的相关信息。
			// 在IE、Firefox、Safri、Opera和Chrome中，document.documentElement.clientWidth和document.documentElement.clientHeight
			// 中保存了页面视口的信息。在IE6中，这些属性必须在标准模式下才有效。如果是混杂模式，就必须通过document.body.clientWidth
			// 和document.body.clientHeight取得相同信息。
			// 虽然最终无法确定浏览器窗口大小，但却可以取得页面视口的大小。
			$(window).resize(function(){
				if (currheight == document.documentElement.clientHeight) {
					return;
				}
				if (resize) {
					clearTimeout(resize);
				}
				resize = setTimeout(function(){
					_runResizeHandlers();
				},50);				//等待50秒直到窗口调整完成。
				currheight = document.documentElement.clientHeight;		//存储最新的窗口高度。
			});
		}else{
			$(window).resize(function(){
				if (resize) {
					clearTimeout(resize);
				}
				resize = setTimeout(function(){
					_runResizeHandlers();
				},50);
			});
		}
	};

	return {

		//初始化主要函数
		init:function(){
			// ！！！ 不要修改这个核心操作调用命令

			//核心操作
			handleInit();		//初始化核心变量
			handleOnResize();	//设置和控制响应

			//UI 组件操作
		},

		//公众函数 为了得到一个参数 以名字从URL中
		getURLParameter:function(paramName){
			//ECMAScript的变量是松散类型的，所谓松散类型就是可以用来保存任何类型的数据。换句话说，
			// 每个变量仅仅是一个用于保存值的占位符而已。
			// 可以使用一条语句定义多个变量，只要向下面这样把每个变量（初始化化或不初始化均可）用逗号隔开即可：
			// 	var message = "hi",
			// 		found = false,
			// 		age = 29;

			// JavaScript substring() 方法
			// substring() 方法用于提取字符串中介于两个指定下标之间的字符。

			// stringObject.substring(start,stop)

			// 参数	描述
			// start	必需。一个非负的整数，规定要提取的子串的第一个字符在 stringObject 中的位置。
			// stop	可选。一个非负的整数，比要提取的子串的最后一个字符在 stringObject 中的位置多 1。如果省略该参数，那么返回的子串会一直到字符串的结尾。

			// JavaScript split() 方法
			// 定义和用法:split() 方法用于把一个字符串分割成字符串数组。
			// 语法:stringObject.split(separator,howmany)
			// 参数	描述
			// separator	必需。字符串或正则表达式，从该参数指定的地方分割 stringObject。
			// howmany		可选。该参数可指定返回的数组的最大长度。如果设置了该参数，返回的子串不会多于这个参数指定的数组。如果没有设置该参数，整个字符串都会被分割，不考虑它的长度。
			// 返回值
			// 一个字符串数组。该数组是通过在 separator 指定的边界处将字符串 stringObject 分割成子串创建的。返回的数组中的字串不包括 separator 自身。
			// 但是，如果 separator 是包含子表达式的正则表达式，那么返回的数组中包括与这些子表达式匹配的字串（但不包括与整个正则表达式匹配的文本）。

			var searchString = window.location.search.substring(1),
			i,val,params = searchString.split("&");

			for (i = 0; i < params.length; i++) {
				val = params[i].split("=");
				if (val[0] == paramName) {
					return unescape(val[1]);
				}
			}
			return null;
		},
	};
}();
