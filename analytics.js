// analytics.js

// Global site tag (gtag.js) - Google Analytics
(function(){
    var gaScript = document.createElement('script');
    gaScript.async = true;
    gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-TF08DB57N6';
    document.head.appendChild(gaScript);
  
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
  
    gtag('config', 'G-TF08DB57N6');
  })();
  