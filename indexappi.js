const apiUrl = "usd";
const proxyUrl = "https://bcra-proxy-cors.vercel.app";
let dataBank = document.querySelector("#dataBank")


fetch(`${proxyUrl}/${apiUrl}`, {
        headers: {
            Authorization: "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTYzODkxODQsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJkaWFuYWRpbmFyb0BnbWFpbC5jb20ifQ.YG6qZuJCnbUsFpcb6Y3jRuWIakOZCc4fCcB2MFdkx8rsOp5KcQDEwVRs6WPA9LisusXb5Z2jKqYWK0KA-PckqQ",
        },
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data)

        const info = data[data.length - 1]


        const content = document.createElement("div")
        content.innerHTML = `<h4> El valor del dolar (USD) a la fecha: ${info.d} es de: ${info.v} ARS </h4>`
        dataBank.append(content)



    })