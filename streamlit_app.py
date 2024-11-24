import streamlit as st

# Set the title of the app
st.set_page_config(page_title="Curriculo - Career Guidance Chatbot", layout="centered")

# Add custom HTML for the app's structure and chatbot integration
st.markdown(
    """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curriculo - Career Guidance Chatbot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #ffffff;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            }
            .button {
                background-color: #ff6347;
                color: white;
                padding: 15px 25px;
                font-size: 18px;
                text-decoration: none;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #ff4500;
            }
            h1 {
                color: #333;
            }
            p {
                color: #555;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Curriculo!</h1>
            <p>Your personalized career guidance chatbot for Under Graduate Students.</p>
        </div>
        <!-- Start of ChatBot (www.chatbot.com) code -->
        <script>
            window.__ow = window.__ow || {};
            window.__ow.organizationId = "864da0d3-9cf9-40d6-b7d9-99e6d65439cc";
            window.__ow.template_id = "ba08368a-3a3a-498f-94b0-7076160ca3b3";
            window.__ow.integration_name = "manual_settings";
            window.__ow.product_name = "chatbot";   
            ;(function(n,t,c){function i(n){return e._h?e._h.apply(null,n):e._q.push(n)}var e={_q:[],_h:null,_v:"2.0",on:function(){i(["on",c.call(arguments)])},once:function(){i(["once",c.call(arguments)])},off:function(){i(["off",c.call(arguments)])},get:function(){if(!e._h)throw new Error("[OpenWidget] You can't use getters before load.");return i(["get",c.call(arguments)])},call:function(){i(["call",c.call(arguments)])},init:function(){var n=t.createElement("script");n.async=!0,n.type="text/javascript",n.src="https://cdn.openwidget.com/openwidget.js",t.head.appendChild(n)}};!n.__ow.asyncInit&&e.init(),n.OpenWidget=n.OpenWidget||e}(window,document,[].slice))
        </script>
        <noscript>You need to <a href="https://www.chatbot.com/help/chat-widget/enable-javascript-in-your-browser/" rel="noopener nofollow">enable JavaScript</a> in order to use the AI chatbot tool powered by <a href="https://www.chatbot.com/" rel="noopener nofollow" target="_blank">ChatBot</a></noscript>
        <!-- End of ChatBot code -->
    </body>
    </html>
    """,
    unsafe_allow_html=True
)
