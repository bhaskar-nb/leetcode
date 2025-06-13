function expect(val)
{
    return{
        toBe: function(expected)
        {
            if(val === expected)
            {
                return true;
            }
            else
            {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(expected)
        {
            if(val !== expected)
            {
                return true;
            }
            else
            {
                throw new Error("Equal");
            }
        }
    };
}

try 
{
    expect(5).toBe(5);
    expect(5).notToBe(10);
    expect(5).toBe(10);
}
catch(error)
{
    console.error(error.message);
}
try
{
    expect(5).notToBe(5);
}
catch(error)
{
    console.error(error.message);
}