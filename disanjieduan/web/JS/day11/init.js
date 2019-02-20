function $(tagName){
		//函数接受字符串参数,表示标签名
		//获取元素节点
		var elem=document.getElementsByTagName(tagName)[0];
		return elem;
	}