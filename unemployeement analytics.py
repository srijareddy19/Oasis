{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <div style=\"color:blue;display:inline-block;border-radius:5px;background-color:#F0E68C;font-family:Nexa;overflow:hidden\"><p style=\"padding:15px;color:blue;overflow:hidden;font-size:100%;letter-spacing:0.5px;margin:0; width:750px;\"><b> </b> Unemployment in India during COVID-19</p></div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **OBJECTIVE**\n",
    "\n",
    "* Unemployment is measured by the unemployment rate which is the number of people who are unemployed as a percentage of the total labour force.\n",
    "* During the Covid-19 period there was a sharp increase in the unemployment rate.\n",
    "* So in this assignment we have to analyze the unemployment rate using Python\n",
    "\n",
    "**Let's get started!!!**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import libraries\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import datetime as dt\n",
    "import calendar\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Region</th>\n",
       "      <th>Date</th>\n",
       "      <th>Frequency</th>\n",
       "      <th>Estimated Unemployment Rate (%)</th>\n",
       "      <th>Estimated Employed</th>\n",
       "      <th>Estimated Labour Participation Rate (%)</th>\n",
       "      <th>Area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>31-05-2019</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>3.65</td>\n",
       "      <td>11999139.0</td>\n",
       "      <td>43.24</td>\n",
       "      <td>Rural</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>30-06-2019</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>3.05</td>\n",
       "      <td>11755881.0</td>\n",
       "      <td>42.05</td>\n",
       "      <td>Rural</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>31-07-2019</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>3.75</td>\n",
       "      <td>12086707.0</td>\n",
       "      <td>43.50</td>\n",
       "      <td>Rural</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>31-08-2019</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>3.32</td>\n",
       "      <td>12285693.0</td>\n",
       "      <td>43.97</td>\n",
       "      <td>Rural</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>30-09-2019</td>\n",
       "      <td>Monthly</td>\n",
       "      <td>5.17</td>\n",
       "      <td>12256762.0</td>\n",
       "      <td>44.68</td>\n",
       "      <td>Rural</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>768 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Region         Date  Frequency   Estimated Unemployment Rate (%)  \\\n",
       "0    Andhra Pradesh   31-05-2019    Monthly                              3.65   \n",
       "1    Andhra Pradesh   30-06-2019    Monthly                              3.05   \n",
       "2    Andhra Pradesh   31-07-2019    Monthly                              3.75   \n",
       "3    Andhra Pradesh   31-08-2019    Monthly                              3.32   \n",
       "4    Andhra Pradesh   30-09-2019    Monthly                              5.17   \n",
       "..              ...          ...        ...                               ...   \n",
       "763             NaN          NaN        NaN                               NaN   \n",
       "764             NaN          NaN        NaN                               NaN   \n",
       "765             NaN          NaN        NaN                               NaN   \n",
       "766             NaN          NaN        NaN                               NaN   \n",
       "767             NaN          NaN        NaN                               NaN   \n",
       "\n",
       "      Estimated Employed   Estimated Labour Participation Rate (%)   Area  \n",
       "0             11999139.0                                     43.24  Rural  \n",
       "1             11755881.0                                     42.05  Rural  \n",
       "2             12086707.0                                     43.50  Rural  \n",
       "3             12285693.0                                     43.97  Rural  \n",
       "4             12256762.0                                     44.68  Rural  \n",
       "..                   ...                                       ...    ...  \n",
       "763                  NaN                                       NaN    NaN  \n",
       "764                  NaN                                       NaN    NaN  \n",
       "765                  NaN                                       NaN    NaN  \n",
       "766                  NaN                                       NaN    NaN  \n",
       "767                  NaN                                       NaN    NaN  \n",
       "\n",
       "[768 rows x 7 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#LOAD DATA SET\n",
    "data = pd.read_csv(\"Unemployment in India.csv\")\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Length mismatch: Expected axis has 7 elements, new values have 9 elements",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32md:\\github\\Unemployment-Analysis-With-Python\\Unemployement-analysis-with-python.ipynb Cell 6\u001b[0m line \u001b[0;36m2\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#W5sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39m#updating the column names\u001b[39;00m\n\u001b[1;32m----> <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#W5sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m data\u001b[39m.\u001b[39mcolumns\u001b[39m=\u001b[39m[\u001b[39m\"\u001b[39m\u001b[39mState\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mDate\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mFrequency\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mEstimated unemployment rate\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mEstimated employed\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mEstimated labour participation rate\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mRegion\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mLongitude\u001b[39m\u001b[39m\"\u001b[39m,\u001b[39m\"\u001b[39m\u001b[39mLatitude\u001b[39m\u001b[39m\"\u001b[39m]\n",
      "File \u001b[1;32mc:\\Users\\Nasar\\anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:5915\u001b[0m, in \u001b[0;36mNDFrame.__setattr__\u001b[1;34m(self, name, value)\u001b[0m\n\u001b[0;32m   5913\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[0;32m   5914\u001b[0m     \u001b[39mobject\u001b[39m\u001b[39m.\u001b[39m\u001b[39m__getattribute__\u001b[39m(\u001b[39mself\u001b[39m, name)\n\u001b[1;32m-> 5915\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mobject\u001b[39;49m\u001b[39m.\u001b[39;49m\u001b[39m__setattr__\u001b[39;49m(\u001b[39mself\u001b[39;49m, name, value)\n\u001b[0;32m   5916\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mAttributeError\u001b[39;00m:\n\u001b[0;32m   5917\u001b[0m     \u001b[39mpass\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\Nasar\\anaconda3\\lib\\site-packages\\pandas\\_libs\\properties.pyx:69\u001b[0m, in \u001b[0;36mpandas._libs.properties.AxisProperty.__set__\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mc:\\Users\\Nasar\\anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:823\u001b[0m, in \u001b[0;36mNDFrame._set_axis\u001b[1;34m(self, axis, labels)\u001b[0m\n\u001b[0;32m    821\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39m_set_axis\u001b[39m(\u001b[39mself\u001b[39m, axis: \u001b[39mint\u001b[39m, labels: AnyArrayLike \u001b[39m|\u001b[39m \u001b[39mlist\u001b[39m) \u001b[39m-\u001b[39m\u001b[39m>\u001b[39m \u001b[39mNone\u001b[39;00m:\n\u001b[0;32m    822\u001b[0m     labels \u001b[39m=\u001b[39m ensure_index(labels)\n\u001b[1;32m--> 823\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_mgr\u001b[39m.\u001b[39;49mset_axis(axis, labels)\n\u001b[0;32m    824\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_clear_item_cache()\n",
      "File \u001b[1;32mc:\\Users\\Nasar\\anaconda3\\lib\\site-packages\\pandas\\core\\internals\\managers.py:230\u001b[0m, in \u001b[0;36mBaseBlockManager.set_axis\u001b[1;34m(self, axis, new_labels)\u001b[0m\n\u001b[0;32m    228\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mset_axis\u001b[39m(\u001b[39mself\u001b[39m, axis: \u001b[39mint\u001b[39m, new_labels: Index) \u001b[39m-\u001b[39m\u001b[39m>\u001b[39m \u001b[39mNone\u001b[39;00m:\n\u001b[0;32m    229\u001b[0m     \u001b[39m# Caller is responsible for ensuring we have an Index object.\u001b[39;00m\n\u001b[1;32m--> 230\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_validate_set_axis(axis, new_labels)\n\u001b[0;32m    231\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39maxes[axis] \u001b[39m=\u001b[39m new_labels\n",
      "File \u001b[1;32mc:\\Users\\Nasar\\anaconda3\\lib\\site-packages\\pandas\\core\\internals\\base.py:70\u001b[0m, in \u001b[0;36mDataManager._validate_set_axis\u001b[1;34m(self, axis, new_labels)\u001b[0m\n\u001b[0;32m     67\u001b[0m     \u001b[39mpass\u001b[39;00m\n\u001b[0;32m     69\u001b[0m \u001b[39melif\u001b[39;00m new_len \u001b[39m!=\u001b[39m old_len:\n\u001b[1;32m---> 70\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mValueError\u001b[39;00m(\n\u001b[0;32m     71\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mLength mismatch: Expected axis has \u001b[39m\u001b[39m{\u001b[39;00mold_len\u001b[39m}\u001b[39;00m\u001b[39m elements, new \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m     72\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mvalues have \u001b[39m\u001b[39m{\u001b[39;00mnew_len\u001b[39m}\u001b[39;00m\u001b[39m elements\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m     73\u001b[0m     )\n",
      "\u001b[1;31mValueError\u001b[0m: Length mismatch: Expected axis has 7 elements, new values have 9 elements"
     ]
    }
   ],
   "source": [
    "#updating the column names\n",
    "data.columns=[\"State\",\"Date\",\"Frequency\",\"Estimated unemployment rate\",\"Estimated employed\",\"Estimated labour participation rate\",\"Region\",\"Longitude\",\"Latitude\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.duplicated().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.State.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Converting \"Date\" column to Datetime format\n",
    "data['Date']= pd.to_datetime(data['Date'],dayfirst=True)\n",
    "\n",
    "#Converting 'Frequency' and 'Region' columns to categorical data type\n",
    "data['Frequency'] = data['Frequency'].astype('category')\n",
    "data['Region'] = data['Region'].astype('category')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Extracting Month From Date attribute**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Month']= data['Date'].dt.month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#converting 'month' to integer format\n",
    "data['Month_int'] = data['Month'].apply(lambda x: int(x))\n",
    "\n",
    "# Mapping integer month values to abbreviated month names\n",
    "data['Month_name'] = data['Month_int'].apply(lambda x: calendar.month_abbr[x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dropping the original 'Month' column\n",
    "data.drop(columns='Month', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['Month'] = data['Month_int'].apply(lambda x: calendar.month_abbr[x])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count":None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Basic Statistics\n",
    "data_stats = data[['Estimated unemployment rate', 'Estimated employed', 'Estimated labour participation rate']]\n",
    "round(data_stats.describe().T, 2)\n",
    "\n",
    "region_stats = data.groupby(['Region'])[['Estimated unemployment rate', 'Estimated employed', \n",
    "                                       'Estimated labour participation rate']].mean().reset_index()\n",
    "round(region_stats, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "IMD = data.groupby([\"Month\"])[['Estimated unemployment rate','Estimated employed','Estimated labour participation rate']].mean()\n",
    "IMD = pd.DataFrame(IMD).reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "month = IMD.Month\n",
    "unemployment_rate = IMD[\"Estimated unemployment rate\"]\n",
    "labour_participation_rate = IMD[\"Estimated labour participation rate\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "fig = go.Figure()\n",
    "\n",
    "fig.add_trace(go.Bar(x=month, y= unemployment_rate, name = \"Unemployment Rate\"))\n",
    "fig.add_trace(go.Bar(x= month , y = labour_participation_rate, name = \"Labourparticipation Rate\"))\n",
    "\n",
    "fig.update_layout(title = \"Unemploymnet Rate and Labour Participation rate \",\n",
    "                 xaxis= {\"categoryorder\":\"array\",\"categoryarray\":[\"Jan\",\"Feb\",\"Mar\",\"Apr\",\"May\",\"Jun\",\"Jul\",\"Aug\",\"Sep\",\"Oct\"]})\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.bar(IMD, x='Month', y='Estimated employed', color='Month',\n",
    "            category_orders = {\"Month\":[\"Jan\",\"Feb\",\"Mar\",\"Apr\",\"May\",\"Jun\",\"Jul\",\"Aug\",\"Sep\",\"Oct\"]},\n",
    "            title = 'Estimated employed people from Jan 2020 to Oct 2020')\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "State = data.groupby(\"State\")[['Estimated unemployment rate','Estimated employed','Estimated labour participation rate']].mean()\n",
    "State = pd.DataFrame(State).reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#box Plot\n",
    "\n",
    "fig = px.box(data,x='State',y='Estimated unemployment rate',color='State',title='Unemployment rate')\n",
    "fig.update_layout(xaxis={'categoryorder':'total descending'})\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "fig = px.bar(State, x='State', y='Estimated unemployment rate', color=\"State\",title=\"Average Unemployment Rate (State)\")\n",
    "fig.update_layout(xaxis={'categoryorder':'total descending'})\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "heat_maps = data[[\"Estimated unemployment rate\", \"Estimated employed\",\"Estimated labour participation rate\",'Longitude','Latitude','Month_int']]\n",
    "heat_maps = heat_maps.corr()\n",
    "plt.figure(figsize=(10,5))\n",
    "sns.set_context(\"notebook\",font_scale=1)\n",
    "sns.heatmap(heat_maps,annot=True , cmap='coolwarm') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count":None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.scatter_matrix(data, template='plotly',\n",
    "                        dimensions=['Estimated unemployment rate', 'Estimated employed', 'Estimated labour participation rate'],\n",
    "                        color='Region')\n",
    "fig.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.bar(data, x='Region', y='Estimated unemployment rate', animation_frame='Month_name', color='State',\n",
    "             title='Unemployment rate across region from Jan.2020 to Oct.2020', height=700, template='plotly')\n",
    "fig.update_layout(xaxis={'categoryorder': 'total descending'})\n",
    "fig.layout.updatemenus[0].buttons[0].args[1][\"frame\"][\"duration\"] = 2000\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sunburst chart showing unemployment rate in each region and state\n",
    "\n",
    "unemplo_df = data[['State', 'Region', 'Estimated unemployment rate', 'Estimated employed', 'Estimated labour participation rate']]\n",
    "unemplo = unemplo_df.groupby(['Region', 'State'])['Estimated unemployment rate'].mean().reset_index()\n",
    "fig = px.sunburst(unemplo, path=['Region', 'State'], values='Estimated unemployment rate',\n",
    "                  color_continuous_scale='Plasma', title='Unemployment rate in each region and state',\n",
    "                  height=650, template='ggplot2')\n",
    "fig.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Impact of Lockdown on States Estimated Employed\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'px' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32md:\\github\\Unemployment-Analysis-With-Python\\Unemployement-analysis-with-python.ipynb Cell 37\u001b[0m line \u001b[0;36m1\n\u001b[1;32m----> <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m fig \u001b[39m=\u001b[39m px\u001b[39m.\u001b[39mscatter_geo(data,\u001b[39m'\u001b[39m\u001b[39mLongitude\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mLatitude\u001b[39m\u001b[39m'\u001b[39m, color\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mRegion\u001b[39m\u001b[39m\"\u001b[39m,\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m                      hover_name\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mState\u001b[39m\u001b[39m\"\u001b[39m, size\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mEstimated unemployment rate\u001b[39m\u001b[39m\"\u001b[39m,\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m                      animation_frame\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mMonth_name\u001b[39m\u001b[39m\"\u001b[39m,scope\u001b[39m=\u001b[39m\u001b[39m'\u001b[39m\u001b[39masia\u001b[39m\u001b[39m'\u001b[39m,template\u001b[39m=\u001b[39m\u001b[39m'\u001b[39m\u001b[39mseaborn\u001b[39m\u001b[39m'\u001b[39m,title\u001b[39m=\u001b[39m\u001b[39m'\u001b[39m\u001b[39mImpack of lockdown on Employement across regions\u001b[39m\u001b[39m'\u001b[39m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m fig\u001b[39m.\u001b[39mlayout\u001b[39m.\u001b[39mupdatemenus[\u001b[39m0\u001b[39m]\u001b[39m.\u001b[39mbuttons[\u001b[39m0\u001b[39m]\u001b[39m.\u001b[39margs[\u001b[39m1\u001b[39m][\u001b[39m\"\u001b[39m\u001b[39mframe\u001b[39m\u001b[39m\"\u001b[39m][\u001b[39m\"\u001b[39m\u001b[39mduration\u001b[39m\u001b[39m\"\u001b[39m] \u001b[39m=\u001b[39m \u001b[39m2000\u001b[39m\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m fig\u001b[39m.\u001b[39mupdate_geos(lataxis_range\u001b[39m=\u001b[39m[\u001b[39m5\u001b[39m,\u001b[39m35\u001b[39m], lonaxis_range\u001b[39m=\u001b[39m[\u001b[39m65\u001b[39m, \u001b[39m100\u001b[39m],oceancolor\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mlightblue\u001b[39m\u001b[39m\"\u001b[39m,\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/github/Unemployment-Analysis-With-Python/Unemployement-analysis-with-python.ipynb#X51sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m     showocean\u001b[39m=\u001b[39m\u001b[39mTrue\u001b[39;00m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'px' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "fig = px.scatter_geo(data,'Longitude', 'Latitude', color=\"Region\",\n",
    "                     hover_name=\"State\", size=\"Estimated unemployment rate\",\n",
    "                     animation_frame=\"Month_name\",scope='asia',template='seaborn',title='Impack of lockdown on Employement across regions')\n",
    "\n",
    "fig.layout.updatemenus[0].buttons[0].args[1][\"frame\"][\"duration\"] = 2000\n",
    "\n",
    "fig.update_geos(lataxis_range=[5,35], lonaxis_range=[65, 100],oceancolor=\"lightblue\",\n",
    "    showocean=True)\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.Region.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "#data representation before and after the lockdown\n",
    "\n",
    "before_lockdown = data[(data['Month_int']>=1) & (data['Month_int']<4)]\n",
    "after_lockdown =  data[(data['Month_int']>=4) & (data['Month_int']<=6)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "af_lockdown=after_lockdown.groupby('State')['Estimated unemployment rate'].mean().reset_index()\n",
    "lockdown= before_lockdown.groupby('State')['Estimated unemployment rate'].mean().reset_index()\n",
    "lockdown['Unemployment Rate before lockdown'] = af_lockdown['Estimated unemployment rate']\n",
    "\n",
    "lockdown.columns=['State','Unemployment Rate Before Lockdown','Unemployment Rate After Lockdown']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "lockdown.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# percentage change in unemployment rate\n",
    "\n",
    "lockdown['rate change in unemployment'] = round(lockdown['Unemployment Rate After Lockdown'] -lockdown['Unemployment Rate Before Lockdown']/lockdown['Unemployment Rate Before Lockdown'],2)\n",
    "plot_per = lockdown.sort_values('rate change in unemployment')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# percentage change in unemployment after lockdown\n",
    "\n",
    "fig = px.bar(plot_per, x='State',y='rate change in unemployment',color='State',\n",
    "            title='percentage change in Unemployment in each state after lockdown',template='ggplot2')\n",
    "fig.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to sort value based on impact\n",
    "\n",
    "def sort_impact(x):\n",
    "    if x <= 10:\n",
    "        return 'impacted States'\n",
    "    elif x <= 20:\n",
    "        return 'hard impacted States'\n",
    "    elif x <= 30:\n",
    "        return 'harder impacted States'\n",
    "    elif x <= 46:\n",
    "        return 'hardest impacted States'\n",
    "    return x\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count":None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot_per['impact status'] = plot_per['rate change in unemployment'].apply(lambda x:sort_impact(x))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count":None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = px.bar(plot_per, y='State',x='rate change in unemployment',color='impact status',\n",
    "            title='Impact of lockdown on employment across states',template='ggplot2',height=650)\n",
    "\n",
    "\n",
    "fig.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "datascience",
   "language": "python",
   "name": "datascience"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}