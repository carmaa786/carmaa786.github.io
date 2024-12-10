export const CTAApi = async (data) => {
 const response1=await fetch("https://cc82c132-219a-4fb6-80ba-8b40d2f70f0f.neodove.com/integration/custom/72e4358b-fa93-4983-a1d4-cea3d4340d97/leads",{
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
    const response = await fetch('https://sxmcshw4rhnmioduf75cgpzw6i0fzlxt.lambda-url.ap-south-1.on.aws/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return response;
  };



  

  export const franchiseApi = async (data) => {
    const response1=await fetch("https://cc82c132-219a-4fb6-80ba-8b40d2f70f0f.neodove.com/integration/custom/1ff3272b-0e84-4961-82a0-2b50d7ff5ed1/leads",{
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
     },
     body: JSON.stringify(data),
   })
       const response = await fetch('https://sxmcshw4rhnmioduf75cgpzw6i0fzlxt.lambda-url.ap-south-1.on.aws/', {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json',
         },
         body: JSON.stringify(data),
       });
       return response;
     };
   
