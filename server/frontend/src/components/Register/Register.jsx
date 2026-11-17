import React,{useState} from "react";
export default function Register(){
 const [form,setForm]=useState({userName:"",firstName:"",lastName:"",email:"",password:""});
 const [message,setMessage]=useState("");
 const change=e=>setForm({...form,[e.target.name]:e.target.value});
 const submit=async e=>{e.preventDefault();setMessage("Registering…");try{
  const r=await fetch("/djangoapp/register",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(form)});
  const data=await r.json();if(r.ok&&data.status==="Authenticated"){sessionStorage.setItem("username",data.userName);window.location.assign("/");}else setMessage(data.error||"Registration failed");
 }catch(err){setMessage("Unable to reach the server.");}};
 return <main className="container py-5" style={{maxWidth:520}}><h1>Create account</h1><form onSubmit={submit} className="vstack gap-3">{[["userName","Username","text"],["firstName","First name","text"],["lastName","Last name","text"],["email","Email","email"],["password","Password","password"]].map(([name,label,type])=><label key={name}>{label}<input className="form-control" name={name} type={type} value={form[name]} onChange={change} required minLength={name==="password"?8:1}/></label>)}<button className="btn btn-primary" type="submit">Register</button></form><p role="status" className="mt-3">{message}</p></main>;
}