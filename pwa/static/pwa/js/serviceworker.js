var CACHE_NAME = 'pwa-cache-v1';
	var urlsToCache = [
		'/',
		'/sw.js',
		'/app.js',
		'/manifest.json',
		'/offline',
		'/static/pwa/images/dino.gif',

		'/static/js/bootstrap.min.css',
		'/static/js/popper.min.js',
		'/static/js/bootstrap.min.js',
		'/static/css/vendor-bundle.css',
		'/static/css/style-azure.css',
		'/static/css/font-awesome-5.13.0.css',
		'/static/css/font-awesome-4.7.0.css',
		'/static/css/smooth-scrow.css',
		'/static/css/back-to-top.css',
		'/static/js/jquery.min.js',
		'/static/js/angular.js',
		'/static/js/jquery-bundle.js',
		'/static/js/scripts.js',
		'/static/js/back-to-top.js',
		'/static/js/bg_particles.js',
		'/static/js/smooth_page_scroll.js',
		'/static/js/jquery.collapser.js',

		];
	const self = this;
	
	// Install SW
	self.addEventListener('install', (event) =>{
		event.waitUntil(
			caches.open(CACHE_NAME)
				.then((cache) => {
					console.log('Opend Cache.');
					
					return cache.addAll(urlsToCache);
				})
			)
	});

	// Listen For requests
	self.addEventListener('fetch', (event) =>{
		event.respondWith(
			caches.match(event.request)
				.then(() => {
					return fetch(event.request)
						.catch(() => caches.match('/offline'))
				})
		)
	});

	// Activate
	self.addEventListener('activate', (event) =>{
		const cacheWhitelist = [];
		cacheWhitelist.push(CACHE_NAME);
	 	event.waitUntil(
			caches.keys().then((cacheNames) => Promise.all(
				cacheNames.map((cacheName) => {
					if (!cacheWhitelist.includes(cacheName)) {
						return caches.delete(cacheName);
						}
					})
				))
			)
	});