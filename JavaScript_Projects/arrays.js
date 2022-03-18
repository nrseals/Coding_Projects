//Push to front, given an array and a value, insert that value at the front of the array w/o built in methods
function pushToFront(arr,val){
    let temp = arr[0];
    for (let i=0;i<=arr.length+1;i++){
        if(i==0){
            arr[0] = val;
        } else {
            let next = arr[i];
            arr[i] = temp;
            temp = next;
        }
    }
}
pushToFront([1,2,3], 0);