

const myComponetn=()=>{

    useEffect(() => {
        let id = setInterval(() => {
            console.log('times is clicked');
        },1000)

        return () => {
            clearInterval(id);
            console.log('timer is cleaned up');
        }
    }, []);
}

export default myComponetn;