import React from 'react'
import { Alert } from 'react-bootstrap'
import Loader from './Loader'

function Message({variant, children}) {
  return (
    <Alert 
        variant={variant}
    >
        {children}
    </Alert>
  )
}

export default Message