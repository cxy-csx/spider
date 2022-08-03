JS对象

```js
function Person(name, age) {
	this.name = name;
	this.age = age;
}

let obj = new Person("zs", 18);

console.log(obj.name);
console.log(obj.age);
```

函数参数

```js
function add(a, b){

	console.log(arguments[0]);
	console.log(arguments[1]);
	
	return a + b;
}

let res = add(1, 5);
console.log(res);
```

自执行函数

方式一

```js
function add(a, b){
	console.log("function exec...");
	return a + b;
}(1, 2);
```

方式二

```js
(function add(a, b){
	console.log("function exec...");
	return a + b;
}(1, 2))
```

方式三

```js
let res = function add(a, b){
    console.log("function exec...");
	return a + b;
}(1, 2);
```

