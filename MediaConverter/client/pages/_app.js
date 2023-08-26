import React, {useEffect, useState} from 'react'
//import { FFmpeg } from '@ffmpeg/ffmpeg';



function _app() {
  const [message, setMessage] = useState("Loading");

  useEffect(()=> {
    fetch("http://localhost:8080/api").then(
      response => response.json()
      ).then(
        data => {
          setMessage(data.message)
          console.log(data)
        }
      )
    
  }, [])

  return (
    <div>_app</div>
  )
}

export default _app
