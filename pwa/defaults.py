from django.conf import settings


def get_pwa_config():
	DEFAULT_CONFIG = {
		"name": "Escrow Teller",
		"short_name": "Escrow Teller",
		"theme_color": "#7820f5",
		"background_color": "#7820f5",
		"display": "standalone",
		"orientation": "any",
		"scope": "/",
		"start_url": "/",
		"icons": [
			{
				"src": "/static/pwa/images/icons/72x72.png",
				"type": "image/png",
				"sizes": "72x72"
			},
			{
				"src": "/static/pwa/images/icons/96x96.png",
				"type": "image/png",
				"sizes": "96x96"
			},
			{
				"src": "/static/pwa/images/icons/128x128.png",
				"type": "image/png",
				"sizes": "128x128"
			},
			{
				"src": "/static/pwa/images/icons/144x144.png",
				"type": "image/png",
				"sizes": "144x144"
			},
			{
				"src": "/static/pwa/images/icons/152x152.png",
				"type": "image/png",
				"sizes": "152x152"
			},
			{
				"src": "/static/pwa/images/icons/192x192.png",
				"type": "image/png",
				"sizes": "192x192"
			},
			{
				"src": "/static/pwa/images/icons/384x384.png",
				"type": "image/png",
				"sizes": "384x384"
			},
			{
				"src": "/static/pwa/images/icons/512x512.png",
				"type": "image/png",
				"sizes": "512x512"
			}
		],
		"lang": "en",
		"dir": "ltr",
		"description": "Blockchain Payment, Data Management & Security Service",
		"version": "1.",
		"manifest_version": "1.0",
		"permissions": [
			"notifications",
			"webRequest"
		],
		"author": "eTeller"
		}
	try:
		if settings.PWA_CONFIG and settings.PWA_CONFIG != {}:
			return settings.PWA_CONFIG
	except:
		return DEFAULT_CONFIG



def get_service_worker():
	SERVICE_WORKER = """
	var CACHE_NAME = 'eteller-v1';
	var urlsToCache = [
		'/',
		'/sw.js',
		'/app.js',
		'/manifest.json',
		'/offline',
        '/static/pwa/img/favicon.png',
		'/static/pwa/img/apple-touch-icon.png',        'https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css',
		'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css',
        'https://www.escrowteller.com/static/pwa/css/style.css',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js',
        'https://www.escrowteller.com/static/pwa/js/main.js',
        '/static/pwa/img/logo.png',
        '/static/pwa/img/hero-img.png',
        '/static/pwa/img/values-1.png',
        '/static/pwa/img/values-2.png',
        '/static/pwa/img/values-3.png',
        '/static/pwa/img/features-3.png',
        '/static/pwa/img/features-2.png',
        '/static/pwa/img/hero-bg.png',
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
	"""
	try:
		if settings.PWA_SW and settings.PWA_SW != {}:
			return settings.PWA_SW
	except:
		return SERVICE_WORKER


def get_app():
	APP = """
	if ("serviceWorker" in navigator) {
		window.addEventListener("load", () => {
			navigator.serviceWorker
			.register("/sw.js")
			.then(res => console.log("service worker registered!"))
			.catch(err => console.log("Your browser support service worker but service worker not registered.", err));
			});
		} else {
			console.log(`Your browser Dosn't Support serviceWorker, so you can't install PWA.`);
		};
	"""
	try:
		if settings.PWA_APP and settings.PWA_APP != {}:
			return settings.PWA_APP
	except:
		return APP

