	if ("serviceWorker" in navigator) {
		window.addEventListener("load", () => {
			navigator.serviceWorker
			.register("/sw.js")
			.then(res => console.log("service worker registered!"))
			.catch(err => console.log("Your browser support service worker but service worker not registered.", err));
			});
		} else {
			console.log(`Your browser Dosn't Support serviceWorker, so you can'n install PWA.`);
		};