import React from 'react'
import { StreamChat } from 'stream-chat';
import { Chat } from 'stream-chat-react';
import Cookies from 'universal-cookie';

import { ChannelListContainer, ChannelContainer } from './components';
import './App.css';

const apiKey = 'ysk7qjpbrrut';

const client = StreamChat.getInstance(apiKey);

const App = () => {
  return (
    <div className="app_wrapper">
        <Chat client={client} theme="team light">
            <ChannelListContainer
            />
            <ChannelContainer
            />

        </Chat>
        <h1>GeoLocation Chat App</h1>
    </div>
  );
}

export default App;