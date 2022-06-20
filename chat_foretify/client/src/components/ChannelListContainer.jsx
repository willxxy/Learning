import React from 'react'
import { ChannelList, useChatContext } from 'stream-chat-react';
import Cookies from 'universal-cookie';
import { ChennelSearch, TeamChannelList, TeamChannelPreview} from './'; 

import GeolocationIcon from '../assets/geolocation.png'

const SideBar = () => (
    <div className="channel-list__sidebar">
        <div className="channel-list__sidebar__icon1">
            <div className="icon1__inner">
                <img src={GeolocationIcon} alt="Geolocation" width="30" />
            </div>
        </div>
    </div>
)

const ChannelListContainer = () => {
  return (
    <div>ChannelListContainer</div>
  );
}

export default ChannelListContainer;
